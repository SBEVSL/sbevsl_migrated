''':mod:`ProJob` --- An extensible module for implementing distributed computational workflows.
========================================================================

.. module:: ProJob
    :platform: OS X, Windows, Linux
    :synopsis: An extensible module for implementing distributed computational workflows.

.. moduleauthor:: Michael R. Bryan <Michael DOT Bryan AT mail DOT rit DOT edu>

'''

# These imports should be cleaned up.
import os
from cPickle import dumps, loads
from time import clock
import types
from threading import Thread, Event, Lock, Semaphore, enumerate as enumThreads
from ProSocket import sockListenerThread, sockSendRecv

PROMOL_DIR_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class BaseComputationStep():
    """.. class:: BaseComputationStep

        BaseComputationStep is the individual unit of a workflow. It is an extensible, callable
        class which takes a BaseTask object as the single mandatory argument. Additional
        keyword arguments may be implemented by the user. The results of the computation
        step should be stored in the task object. The return code of the computation step should
        indicate whether the workflow should continue, '1' or terminate, '0'.

"""
    def __init__(self, computationName='identity'):
        """.. method:: __init__(self, computationName='identity')

            The __init__ method for BaseComputationStep stores the name of the computation step.

        """
        self.computationName = computationName

    def __call__(self, task, **kwargs):
        """.. method:: __call__(self, task, **kwargs)

            Overriding __call__ makes BaseCompuationStep a callable object. Thus, the computation
            step is executed by calling the step like a function, with the task object as the argument:

            'returncode = BaseComputationStep(taskObject)'

            Calling BaseComputationStep on a task will leave the task unchanged. This function
            should be overridden by extending classes to impart meaningful behavior.

        """
        return 1

class BaseWorkflow():
    """.. class:: BaseWorkflow

        BaseWorkflow is an extensible, callable class which executes a sequence of
        ComputationSteps when called on a BaseTask object. The BaseTask object stores the
        results of all computation steps throughout the workflow. A workflow should return '1' if all
        compuation steps were completed or '0' if the workflow was truncated.

    """

    def __init__(self, workflowName='identity', computationSteps=[BaseComputationStep()]):
        """.. method:: __init__(self, workflowName='identity', computationSteps=[BaseComputationStep()])

            The BaseWorkflow is initialized with the workflow name and the list of computation steps
            to be executed.

        """
        self.workflowName = workflowName
        self.computationSteps = computationSteps

    def __call__(self, task, **kwargs):
        """.. method:: __call__(self, task, **kwargs)

            BaseWorkflow overrides __call__ to become a callable class. A workflow is executed
            of a task by treating the workflow like a function and passing the task as an argument:

            'returncode = BaseWorkflow(task)'

        """
        for computation in self.computationSteps:
            print computation.computationName
            if computation(task, **kwargs): continue
            else: return 0
        else: return 1

class BaseTask(dict):
    """.. class:: BaseTask(dict)

        BaseTask extends the python dictionary class, 'dict'. Arbitrary data may be stored and
        retrieved from the task throughout the workflow. To facilitate transfer of tasks through
        inter-process communication, BaseTask provides methods for serialization using python's
        cPickle module.

    """
    KEY_ERROR_RETURN_VALUE = 'N/A'
    
    def __init__(self, name='identity', batchName='batch', workflow='BaseWorkflow'):
        """.. method:: __init__(self, name='identity', workflow='BaseWorkflow')

            A BaseTask is intialized with a task name and the workflow name it is intended for. 

        """
        dict.__init__(self)
        self.update({'name' : name,
                     'batchName' : batchName,
                     'Workflow' : workflow})

    def __getitem__(self, key):
        """.. method:: __getitem__(self, key)

            __getitem__ determines how BaseTask accomodates value retrieval of the form:

            'value = BaseTask[key]'

            Overridding __getitem__ allows control over the KeyError behavior of the underlying
            dictionary when a key is not already present. In this case, instead of raising KeyError,
            BaseTask will return the value of class variable 'KEY_ERROR_RETURN_VALUE', currently
            assigned 'N/A'.

        """
        try: return dict.__getitem__(self, key)
        except KeyError: return BaseTask.KEY_ERROR_RETURN_VALUE

    def serialize(self, protocol=0):
        """.. method:: serialize(self, protocol=0)

            The BaseTask data structure is serialized to an ASCII string using the python module
            cPickle. To facilitate identification without unpickling, the name of the task is exposed
            at the head of the pickled string.

        """
        return '%s!%s' % (self['name'], dumps(self, protocol=protocol))

    @staticmethod
    def deserialize(serializedTask):
        """.. method:: deserialize(serializedTask)

            A serialized task may be unpickled by calling the static method 'deserialize'. This method
            will ignore any augmented data.

        """
        return loads(serializedTask.split('!',2)[1])

    @staticmethod
    def augment(serializedTask, serializedData):
        """.. method:: augment(serializedTask, serializedData)

            A serialized task may be augmented with additional serialized data using the static
            method 'augment'.

        """
        return '!'.join([serializedTask, serializedData])

    @staticmethod
    def deserializeAugmented(serializedTask):
        """.. method:: deserializeAugmented(serializedTask)

            The static method 'deserializeAugmented' will deserialize both the task and the
            augmented data, returning a list in which the task is at index, '0'.

        """
        return [loads(s) for s in serializedTask.split('!')[1:]]

    @staticmethod
    def serializedName(serializedTask):
        """.. method:: serializedName(serializedTask)

            The static method 'serializedName' will return the name of a serialized task without
            deserializing the data structure.

        """
        return serializedTask.split('!',1)[0]

    @staticmethod
    def serializedAddr(serializedTask):
        """.. method:: serializedAddr(serializedTask)

            The static method 'serializedAddr' will return the client return address tuple of the task
            -- (host, port) -- without deserializing the data structure.

        """
        return (lambda x: (x[0], int(x[1])))(serializedTask.split('!',1)[0].split(':',1)[1].split('/',1))

    @staticmethod
    def serializedNameAddr(serializedTask):
        """.. method:: serializedNameAddr(serializedTask)

            The static method 'serializedNameAddr' will return a tuple of the task name and client
            return address -- (name, (host, port)) -- without deserializing the data structure.

        """
        return (lambda x: (x, (lambda y: (y[0], int(y[1])))(x.split(':',1)[1].split('/',1))))(serializedTask.split('!',1)[0])                          

class DefaultProMolTask(BaseTask):
    """.. class:: DefaultProMolTask(BaseTask)

        DefaultProMolTask extends BaseTask to provide functionality specific to the default ProMol
        workflow. The class variable 'resultFields' specifies an ordered list of fields that would appear
        as the header of a CSV file for the results of a batch. As a class variable, this field is not pickled
        with the task during serialization. BaseTask extends python's dictionary class, so each string in
        the 'resultFields' list should be the key to its corresponding result value.  

    """
    
    resultFields = ['Query Class [EC,pfam,etc.]', 'Motif','Query PDB ID', 'Precision factor','Substitutions', 'Levenshtein dist. [# of edits]',
            'IDSpec by residue [# of residues]', 'Chain count [# in structure]', 'Super RMSD [A]', 'Super match [# of residues]',
            'Motif size [# of residues]', 'Super match difference [# of residues]', 'CEAlign RMSD [A]',
            'CEAlign match [# of atoms]', 'Motif size [# of atoms]', 'CEAlign match difference [# of atoms]',
            'Fetch time [sec]', 'MotifCaller() runtime [sec]', 'count() & levenshteinDistance() runtime [sec]',
            'SuperAlign runtime [sec]', 'CEAlign runtime [sec]', 'Total runtime [sec]', 'MotifCaller() runtime [%]',
            'IDSpec: Motif Interatomic Distance Spectra', 'MotifCaller() residues'
            ]

    def __init__(self, pdb, motif, returnAddr, batchName=None, name=None, d=1.0,
            queryClass=None, subs=False, workflow='DefaultProMolWorkflow'):
        """.. method:: __init__(self, pdb, motif, returnAddr,
                                                       name=None,
                                                       d=1.0,
                                                       queryClass=None,
                                                       subs=False,
                                                       workflow='DefaultProMolWorkflow')

            The DefaultProMolTask is initialized with mandatory arguments:
                'pdb' := The PDB ID of the query protein structure.
                'motif' := The name of the motif that will be run against this structure.
                'returnAddr' := The return address tuple of the client who submits this task, (host, port).
            Optional arguments:
                'name' := The name of the task is optional and will default to a combination of pdb, motif, d,
                        and returnAddr which uniquley identifies the task to both client and servers.
                'd' := The Precision value for this task. Default is currently '1.0'.
                'queryClass' := The class of the query protein structure [ EC #, pfam ID, etc... ].
                'subs' := A boolean indicating whether substitutions should be performed for this task.
                        The default is 'False'.
                'workflow' := The intended workflow for this task defaults to 'DefaultProMolWorkflow'.

        """
        BaseTask.__init__(self,
                          name='{0}/{1}/{2}:{3[0]}/{3[1]}'.format(pdb,motif,d,returnAddr),
                          batchName=batchName,
                          workflow=workflow)
        self.update({'Return Address' : returnAddr,
                        'Query Class [EC,pfam,etc.]' : queryClass,
                        'Motif' : motif,
                        'Query PDB ID' : pdb,
                        'Precision factor' : d,
                        'Substitutions' : subs
                        })

    def __str__(self):
        """.. method:: __str__(self)

            This function overrides the string coercion behavior for DefaultProMolTask. The default
            behavior is to return a semicolon-delimited string of the result field values. If a result does
            not exist, the field is populated with 'N/A'.

            Future work: Allowing default delimiter and keyErrorValue to be overridden by __str__
            function arguments.

        """
        delimiter = ';'
        string = ''
        for field in self.resultFields:
            value = `self[field]`
            string += '%s%s'%(value, delimiter)
        return string[:-1]

class BaseJobExecutor():
    """.. class:: BaseJobExecutor

        BaseJobExecutor is an extensible, callable class which instantiates the fundamental
        components for submitting a job to the remote ServerManager or local ProServer
        instance.

    """
    
    def __init__(self,
                 serverPort,
                 serverHost='127.0.0.1',
                 host='127.0.0.1',
                 maxSimultaneousBatches=50,
                 shutdownFunc=(lambda x: False)):
        """.. method:: __init__(self, serverPort,
                                                     serverHost='127.0.0.1',
                                                     host='127.0.0.1',
                                                     maxSimultaneousBatches=50,
                                                     shutdownFunc=(lambda x: False))

            When initialized, the BaseJobExecutor launches a result listener thread, partitions the
            job into batches of tasks, submits batches sequentially, and processes the results. If
            this is a non-distributed job, a local instance of ProServer is instantiated.
            Batches should aggregate tasks in a way that exploits their sequential serial submission to
            the ServerManager/ProServer. However, each batch is submitted with a separate
            thread, so that results may be recieved asynchronously. Thus the argument,
            'maxSimultaneousBatches' determines the maximum number of simultaneous threads
            awaiting results. The current default is arbitrarily set to 50. The optimal value is a function
            of batch size, instantaneous task throughput and is constrained by client-specific
            hardware/software parameters.

        """
        try:
            # this code will query the ServerManager for availability and load of the
            # distributed framework. If the Server Manager is unavailable or the serverPort
            # is specified less than or equal to 0, a local server instance is launched.
            raise Exception()
            if serverPort <= 0: raise
        except Exception as err:
            print 'BaseJobExecutor:', err
            from ProServer import BaseProServer # buried imports are not a best practice
            self.localServer = BaseProServer(shutdownFunc)
            #self.localServer.setDaemon(True)
            self.localServer.start()
            self.submitBatch = self.submitBatchLocal
        else:
            self.submitBatch = self.submitBatchDistributed
            
        self.jobResultCallables = {'r' : (lambda data,sock,addr:
                                          Thread(target=self.processTaskResult,
                                          args=(data[1:],sock)).start() and 0 or '0')}
        self.host = host
        self.resultPort = 0
        self.resultPortSetEvent = Event()
        self.result = {}
        self.resultCount = {}
        self.resultMutex = Lock()
        self.serverHost = serverHost
        self.serverPort = serverPort
        self.shutdown = shutdownFunc
        self.resultListenerThread = Thread(target=self.jobResultListener)
        self.resultListenerThread.setDaemon(True)
        self.resultListenerThread.start()
        self.submissionMutex = Lock()
        self.maxSimultaneousSemaphore = Semaphore(maxSimultaneousBatches)

    def __call__(self, **kwargs):
        """.. method:: __call__(self, **kwargs)

            BaseJobExecutor is callable with keyword arguments, that are passed on to
            createTaskBatches. 

        """
        self.resultPortSetEvent.wait()
        self.resultAddr = (self.host, self.resultPort)
        print 'resultAddr:',self.resultAddr #p#
        for num, (batchName, batch) in enumerate(self.createTaskBatches(**kwargs).iteritems()):
            self.maxSimultaneousSemaphore.acquire()
            self.submissionMutex.acquire()
            try:
                if self.shutdown():
                    break
            except BaseException as err: print err
            batchThread = Thread(target=self.batchExecutor, args=(batchName, batch), name='be')
            batchThread.start()
            #p#print '{0}:: {1}'.format(batchName, num+1) #p#
        while not self.shutdown(timeout=5.0):
            for jobEx in enumThreads():
                if jobEx.getName() == 'be' and jobEx.isAlive(): break
            else:
                return 1

    def batchExecutor(self, batchName, batch):
        """.. method:: batchExecutor(self, batchName, batch)

            The batch executor thread submits a batch of tasks to the ServerManager or local
            ProServer instance. Subsequently, it releases the submissionMutex lock so the
            next batch may be submitted. Then, the thread sleeps for long intervals until all of
            the results are returned. Finally, when the batch is complete, it calls the
            processBatchResult method.

        """
        self.result[batchName] = []
        try:
            self.resultCount[batchName] = 0
            batchSize = len(batch) #1
            self.submitBatch(batch)
            self.submissionMutex.release()
            while not self.shutdown(timeout=15.0):
                count = self.resultCount[batchName]
                # update progress bar code
                #if count: print '{0}: {1}/{2}'.format(batchName, count, batchSize)
                if count >= batchSize:
                    #print '{0} Done.'.format(batchName)
                    break
        finally:
            if len(self.result[batchName]):
                self.processBatchResult(batchName)
                self.resultMutex.acquire()
                try:
                    del self.result[batchName], self.resultCount[batchName]
                finally:
                    self.resultMutex.release()
            self.maxSimultaneousSemaphore.release()

    def submitBatchLocal(self, batch):
        """.. method:: submitBatchLocal(self, batch)

            This method will submit the batch of tasks to the local ProServer instance.

        """
        for task in batch:
            self.localServer.addTask(task)

    def submitBatchDistributed(self, batch):
        """.. method:: submitBatchDistributed(self, batch)

            This method will submit the batch of tasks to the remote ServerManager.

        """
        sockSendRecv('j{0}'.format(dumps(batch, protocol=0)),
                         self.serverPort, host=self.serverHost)
        
    def setResultPort(self, port):
        """.. method:: setResultPort(self, port)

            This method is passed as an argument for sockListenerThread during instantiation of
            the job result listener. After the operating system assigns an available port the listener,
            its value is available for specifying each task's return address.

        """
        self.resultPort = port
        self.resultPortSetEvent.set()

    def createTaskBatches(self, **kwargs):
        """.. method:: createTaskBatches(self, **kwargs)

            This method takes the keyword arguments passed while calling BaseJobExecutor.
            Currently, this method must be overridden by extending classes. A batch is defined as a
            list of objects which instantiate an extension of the class BaseTask. This method must
            return a list of batches.

        """
        print 'BaseJobExecutor.createTaskBatches(**kwargs) must be overridden by extending classes.'

    def jobResultListener(self):
        """.. method:: jobResultListener(self)

            This method instantiates a sockListenerThread from the ProSocket module.
        """
        sockListenerThread(portSetTarget=self.setResultPort,
                           workerCallables=self.jobResultCallables,
                           shutdownTarget=self.shutdown)
        print 'jrl shutdown'

    def processTaskResult(self, resultsStr, sock):
        """.. method:: processTaskResult(self, resultStr, sock)
  
            This method will recieve a serialized list of serialized task results. It is intended to be
            overridden by extending classes.
        """
        for serializedTask in loads(resultsStr):
            task = BaseTask.deserialize(serializedTask)
            print task['name'] 

    def processBatchResult(self, batchName, **kwargs):
        """.. method:: processBatchResult(self, batchName)

            This method will receive the name of a completed batch, and is called just prior to
            deleting the results for this batch. It is intended to be overridden by extending classes.

        """
        print '%s Complete.'%batchName

    def join(self):
        """.. method:: join(self)

            Calling this method allows the local server thread to be joined during shutdown.

        """
        try: self.localServer.join()
        except: return

class DefaultProMolJobExecutor(BaseJobExecutor):
    """.. class:: DefaultProMolJobExecutor(BaseJobExecutor)

        DefaultProMolJobExecutor extends BaseJobExecutor to implement the default ProMol
        query: searching for a set of motifs within a set of query protein structures.

        Perhaps this class should be implemented in Motif.py, where the GUI can be updated
        directly.

    """
    def __init__(self,
                 serverPort,
                 shutdownFunc,
                 serverHost='127.0.0.1',
                 host='127.0.0.1',
                 outputDir=None):
        """.. method:: __init__(self, serverPort, shutdownFunc, serverHost='127.0.0.1', host='127.0.0.1', distributed=0)

            The __init__ method for DefaultProMolJobExecutor calls the __init__ method of
            BaseJobExecutor. If this is a distributed Job, the 'serverPort' for the ServerManager
            must be provided. If the serverHost and host IP addresses are not specified, they default
            to localhost, '127.0.0.1'. Finally, if 'distributed' is '1', the JobExecutor will attempt to
            submit the job to a remote ServerManager.

        """
        BaseJobExecutor.__init__(self,
                                 serverPort,
                                 serverHost='127.0.0.1',
                                 host='127.0.0.1',
                                 shutdownFunc=shutdownFunc)
        self.outputDir = outputDir

    def createTaskBatches(self, pdbs, motifs, d):
        """.. method:: createTaskBatches(self, pdbs, motifs, d)

            In DefaultProMolJobExecutor, the createTaskBatches method overrides the
            BaseJobExecutor method of the same name. Each ProMol Batch corresponds to a
            single Query PDB ID. A batch contains one task for each Motif run against the Query
            protein.

        """
        return {pdb : [DefaultProMolTask(pdb,
                                         motif,
                                         self.resultAddr,
                                         batchName=pdb,
                                         d=d,
                                         queryClass=pdbs[pdb]).serialize()
                       for motif in motifs
                       ]
                for pdb in pdbs
                }

    def processTaskResult(self, resultsStr, sock):
        """.. method:: processTaskResult(self, resultsStr, sock)

            In DefaultProMolJobExecutor, the processTaskResult method overrides the BaseJobExecutor
            method of the same name. For each task returned, some data are
            reported to STDOUT and the task is stored in the results dictionary by Query PDB ID.

            This method should by modified to merge with motif.py

        """
        for serializedTask in loads(resultsStr):
            task = BaseTask.deserialize(serializedTask)
            try:
                print task['Query PDB ID'], task['Motif'], task['Total runtime [sec]']
                try: print task['Fetch time [sec]']
                except: pass
                print task['IDSpec by residue [# of residues]']
                superDiff = task['Super match difference [# of residues]']
                ceDiff = task['CEAlign match difference [# of atoms]']
                print superDiff, ceDiff
            except BaseException as err: print err
            self.resultMutex.acquire()
            try: # critical region
                self.result[task['batchName']].append(task)
                self.resultCount[task['batchName']] += 1
            finally: # always release the lock
                self.resultMutex.release()

    def processBatchResult(self, batchName):
        """.. method:: processBatchResult(self, batchName)

            In DefaultProMolJobExecutor, the processBatchResult method overrides the BaseJobExecutor
            method of the same name. When a batch is completed, all of the results are written to
            a designated output file.

            This method should be modified to merge with motif.py.

        """
        outputFile = os.path.join(self.outputDir, '{0}_results.txt'.format(batchName))
        with open(outputFile ,'w') as fout:
            fout.write(';'.join(DefaultProMolTask.resultFields)+'\n')
            for task in self.result[batchName]:
                fout.write('{!s}\n'.format(task))
        #print 'Results saved to', outputFile

class MotifCallerStep(BaseComputationStep):
    """.. class:: MotifCallerStep(BaseComputationStep)

        MotifCallerStep executes the motif file to select residues in the query structure which
        which satisfy the interatomic distance spectra (IDSpec) of the motif.

        Perhaps this class should be implemented in TaskExecutor.py to cercumvent
        unorthodox import statements.

    """
    
    def __init__(self, aminoHashTable, cmd, stored, fetchPath):
        """.. method:: __init__(self, aminoHashTable, cmd, stored, fetchPath)

            MotifCallerStep is instantiated with arguments for the PyMOL API modules 'cmd' and
            'stored', as well as the 'aminoHashTable' and 'fetchPath' from promolglobals.
                  
        """
        BaseComputationStep.__init__(self, computationName='MotifCallerStep')
        self.aminoHashTable = aminoHashTable
        self.cmd = cmd
        self.stored = stored
        self.currPDB = None
        self.fetchPath = fetchPath

    def __call__(self, task):
        """.. method:: __call__(self, task)

            Copied/modified from MotifCaller() to avoid the import statments of motif.py, allowing
            for execution within a no-GUI PyMOL instance.
           
        """
        returncode = 0
        if self.currPDB != task['Query PDB ID']:
            task['Fetch time [sec]'] = clock()
            self.cmd.reinitialize()
            #self.cmd.load(os.path.join(self.fetchPath, task['Query PDB ID']+'.pdb'))
            self.cmd.fetch(task['Query PDB ID'], async=0, path=self.fetchPath)
            task['Fetch time [sec]'] = clock() - task['Fetch time [sec]']
            self.currPDB = task['Query PDB ID']
        try:
            task['MotifCaller() runtime [sec]'] = clock()
            self.cmd.hide('everything', 'all')
            self.cmd.remove("all and hydro")
            motif = task['Motif']
            print motif
            subs = task['Substitutions']
            d = task['Precision factor']
            cmd = self.cmd
            resSelectionSubs = self.resSelectionSubs
            IDSpec = task['IDSpec: Motif Interatomic Distance Spectra'] = {}
            try:
                execfile(task['motifData']['path'])
            except BaseException as err: print err
            if (motif not in self.cmd.get_names('all')):
                print 'motifCaller({0}): motif not in namespace.'.format(motif)
                raise Warning
            elif(self.cmd.count_atoms(motif) == 0):
                print 'motifCaller({0}): count is 0.'.format(motif)
                raise Warning
            else:
                num_of_residues = 0
                if motif[0] is 'S':
                    task['IDSpec by residue [# of residues]'] = {id.split('_',1)[1] : count
                                                             for id, count in task['IDSpec: Motif Interatomic Distance Spectra'].items()
                                                             if isinstance(id, types.StringTypes) and id.startswith('r_')
                                                             }
                    num_of_residues = reduce(lambda x,y: x+(1 if y else 0), task['IDSpec by residue [# of residues]'].values(), 0)
                else:
                    for resn in set(task['motifData']['resi']):
                        num_of_residues += cmd.count_atoms('n. %s&%s'%(self.aminoHashTable[resn]['m'][0], motif))
                if  num_of_residues < 2:
                    print 'motifCaller({0}): fewer than 2 residues'.format(motif)
                    raise Warning
                try: task['Chain count [# in structure]'] = len(self.cmd.get_chains(motif))
                except BaseException as err: print err
                returncode = 1
        except Warning: returncode = 0
        else: pass
        finally:
            task['MotifCaller() runtime [sec]'] = clock() - task['MotifCaller() runtime [sec]']
            print returncode
            return returncode

    def resSelectionSubs(self, resn, atom=False, subs=False, selection=False):
        """.. method:: resSelectionSubs(self, resn, atom=False, subs=False, selection=False)

            This method enables substitutions to occur within the 'S' set motifs.
           
        """
        resnCode = resn.split('_')[0]
        atomIndex = 0
        #p#print atom, resn, minimalAtomList[resnCode] #p#
        if atom: atomIndex = self.aminoHashTable[resnCode]['m'].index(atom) #minimalAtomList[resnCode].index(atom)
        else: atom = self.aminoHashTable[resnCode]['m'][atomIndex] #minimalAtomList[resnCode][atomIndex]
        #p#print atom, resn, minimalAtomList[resnCode] #p#
        if subs:
            resnList = [resnCode]
            try: resnList.append(self.aminoHashTable[resnCode]['s']) # would like to make this 'extend', mind the createSub dependency
            except KeyError: pass
            subSele = '(%s)'%('|'.join(['(n. %s&r. %s)'%(self.aminoHashTable[r]['m'][atomIndex],r) for r in resnList]))
            if selection: return '(%s&%s)'%(subSele,resn)
            else: return subSele
        else:
            #p#print 'n. %s&%s'%(atom,resn) if selection else 'n. %s&r. %s'%(atom,resn) #p#
            return 'n. %s&%s'%(atom,resn) if selection else 'n. %s&r. %s'%(atom,resn)

class CountLevDistStep(BaseComputationStep):
    """.. class:: CountLevDistStep(BaseComputationStep)

        This computation step executes the Count() method from motif.py. The Count() method
        calls the LevenshteinDistance() method from proutils.py. If these methods were imported
        from their respective modules, importing would trigger execution of the ProMol GUI import
        statements within both motif.py and proutils.py. The ProMol GUI is not desireable for
        execution of a light-weight motif finder within a no-GUI PyMOL instance. The expedient
        solution was to copy these methods into this class.

        Future work: enabling the import of the Count() and LevenshteinDistance() methods,
        instead of creating copies in this class.

        Perhaps this class should be implemented in TaskExecutor.py to cercumvent
        unorthodox import statements.

    """
    def __init__(self, aminoHashTable, cmd, stored):
        """.. method:: __init__(self, aminoHashTable, cmd, stored)

            This computation step is instantiated with arguments which provide access to the PyMOL
            API modules 'cmd' and 'stored', as well as the 'aminoHashTable' from promolglobals.
              
        """
        BaseComputationStep.__init__(self, computationName='CountLevDistStep')
        self.aminoHashTable = aminoHashTable
        self.cmd = cmd
        self.stored = stored

    def __call__(self, task):
        """.. method:: __call__(self, task)

            When called, the task is updated with the list of residues selected within the query structure
            by the MotifCallerStep and the LevenshteinDistance between this list and the list of residues
            comprising the motif.
              
        """
        task['count() & levenshteinDistance() runtime [sec]'] = clock()
        try: self.count(task)
        except BaseException as err: print err
        finally:
            task['count() & levenshteinDistance() runtime [sec]'] = clock() - task['count() & levenshteinDistance() runtime [sec]']
            return 1

    def count(self, task):
        """.. method:: count(self, motif, pdb, motifData)

            Copied/modified to avoid the import statments of motif.py, allowing for execution within
            a no-GUI PyMOL instance.
            
        """
        try: 
            last = None
            ordered = []
            orderedchain = {}
            bannedchain = []
            self.stored.motif = []
            editdist = []
            try:
                self.cmd.iterate(task['Motif'], 'stored.motif.append((chain,resn,resi))')
            except BaseException as err: print err
            residues = task['motifData']['resi'] # glb.MOTIFS[motif]['resi']
            residuesl = len(residues)*2
            task['MotifCaller() residues'] = []
            task['Levenshtein dist. [# of edits]'] = '' # glb.GUI.motifs['csvprep'][pdb][motif]['res'] = []
            for iteration in self.stored.motif:
                if last != iteration:
                    last = iteration
                    task['MotifCaller() residues'].append(iteration) # glb.GUI.motifs['csvprep'][pdb][motif]['res'].append(iteration)
                    ordered.append(iteration[1].lower())
                    if iteration[0] not in orderedchain:
                        if iteration[0] not in bannedchain:
                            orderedchain[iteration[0]] = []
                        else:
                            continue
                    orderedchain[iteration[0]].append(iteration[1].lower())
                    if residuesl <= len(orderedchain[iteration[0]]):
                        bannedchain.append(iteration[0])
                        del orderedchain[iteration[0]]
            if len(orderedchain) == 0 and residuesl <= len(ordered):
                ##log('count() return None:: len(orderedchain): {0}; residuesl: {1} <= len(ordered): {2}; resList: {3}.'.format(len(orderedchain),
                ##                                                                          residuesl, len(ordered), resList))
                task['Levenshtein dist. [# of edits]'] += 'N1_' #return None
            substitutions = [None]
            if task['Motif'][0] == 'J':
                for c in ('asp','glu','asn','gln','thr','ser'):
                    if c in residues:
                        substitutions = self.createsubs(residues)
                        break
            for chain in orderedchain:
                editdist.append(self.levenshteinDistance(residues,orderedchain[chain]))
                for sub in substitutions:
                    if sub == None:
                        break
                    editdist.append(self.levenshteinDistance(sub,orderedchain[chain]))
            editdist.append(self.levenshteinDistance(residues,ordered))
            for sub in substitutions:
                if sub == None:
                    break
                editdist.append(self.levenshteinDistance(sub,ordered))
            mini = min(editdist)
            maxi = max(editdist)
            if (residuesl < 6 and mini > 0) or (residuesl < 12 and mini > 1) or \
                   (residuesl < 18 and mini > 2) or mini > 3:
                ##log('Count() return None:: residuesl: {0}; mini: {1}; maxi: {2}; resList: {3}.'.format(residuesl, mini, maxi, `resList`))
                task['Levenshtein dist. [# of edits]']  += 'N2_' #return None
            #glb.GUI.motifs['csvprep'][pdb][motif]['levdistrange'] = '{0}-{1}'.format(mini,maxi) if mini<maxi else mini
            task['Levenshtein dist. [# of edits]']  += '%s-%s'%(mini,maxi) if mini<maxi else `mini`
            # Removed storage of precision factor as it is the same for the entire search
            #print 'ldr:{0}, rl:{1}'.format(mini, resList)
            ##log('count() return ldr:: residuesl: {0}; mini: {1}; maxi: {2}; resList: {3}.'.format(residuesl, mini, maxi, `resList`))
            return 1
        except BaseException as err: print err

    # Returns the edit distance between its arguments
    def levenshteinDistance(self,x,y):
        """.. method:: levenshteinDistance(x,y)

           Copied to avoid the import statments of proutils.py, allowing
           for execution within a no-GUI PyMOL instance.
           
        """
        w,h = len(x)+1,len(y)+1
        #x+1 rows and y+1 columns
        matrix = [ [None]*h for i in range(w) ]
        for i in range(w):
            matrix[i][0] = i
        for j in range(h):
            matrix[0][j] = j
        for j in range(1,h):
            for i in range(1,w):
                if x[i-1] == y[j-1]:
                    matrix[i][j] = matrix[i-1][j-1]
                else:
                    #deletion,insertion,substitution
                    matrix[i][j] = min(matrix[i-1][j]+1,matrix[i][j-1]+1,
                        matrix[i-1][j-1]+1)
        return matrix[w-1][h-1] #edit distance

    # Returns a list of amino acid lists which could be considered
    # equivalent to the sequence argument (all possible permutations)
    def createsubs(self,tup):
        """.. method:: createsubs(tup)

            Copied to avoid the import statments of proutils.py, allowing
            for execution within a no-GUI PyMOL instance.
            
        """
        matrix = [[]]
        for acid in tup:
            newMatrix = []
            for subList in matrix:
                identical = subList[:] # Slice copy as shown on http://docs.python.org/tutorial/controlflow.html section 4.2
                identical.append(acid)
                newMatrix.append(identical)
                if 's' in self.aminoHashTable[acid]:
                    substituted = subList[:]
                    substituted.append(self.aminoHashTable[acid]['s'])
                    newMatrix.append(substituted)
            matrix = newMatrix
        return matrix

class SuperCEAlignStep(BaseComputationStep):
    """.. class:: SuperCEAlignStep(BaseComputationStep)

        This computational step calculates the number of motif residues aligned to the
        query protein structure, and the RMSD of that alignment.

        Perhaps this class should be implemented in TaskExecutor.py to cercumvent
        unorthodox import statements.

    """
    def __init__(self, aminoHashTable, cmd, stored, fetchPath):
        """.. method:: __init__(self, aminoHashTable, cmd, stored, fetchPath)

            This computational step is instantiated with arguments providing access to the PyMOL
            API modules 'cmd' and 'stored', as well as the 'aminoHashTable' and 'fetchPath' from
            promolglobals.
              
        """
        BaseComputationStep.__init__(self, computationName='SuperCEAlignStep')
        self.aminoHashTable = aminoHashTable
        self.cmd = cmd
        self.stored = stored
        self.fetchPath = fetchPath

    def __call__(self, task):
        """.. method:: __call__(self, task)

            Copied / modified from getRMSD() to avoid the import statments of proutils.py,
            allowing for execution within a no-GUI PyMOL instance.
            
        """
        motif = task['Motif']
        motifPDBCode = motif.split('_',2)[1]
        queryPDBCode = task['Query PDB ID']
        task['Motif size [# of residues]'] = len(task['motifData']['resi'])
        try:
            querySubsetName = 'match_in_%s'%(queryPDBCode)
            self.cmd.select(querySubsetName, motif)
            self.cmd.hide('everything', 'all')
            if queryPDBCode == motifPDBCode:
                motifPDBCode = '%s%s' %(motifPDBCode, 1)
                self.cmd.copy(motifPDBCode, queryPDBCode)
            else:
                self.cmd.fetch(motifPDBCode, async=0, path=self.fetchPath)
            motifSubsetName = 'match_in_%s'%(motifPDBCode)
            task['Motif size [# of atoms]'] = self.cmd.select(motifSubsetName, '%s and (%s)' % (motifPDBCode,
                                                         task['motifData']['loci']))
            self.cmd.hide('everything', 'all')
            #aligns and gets the rmsd of the alignment. # of atoms in each selection must be greater than 5
            task['SuperAlign runtime [sec]']  = clock()
            try:
                superAlign = self.cmd.super(motifSubsetName, querySubsetName, quiet=0)
                if superAlign[1]:
                    task['Super RMSD [A]'] = superAlign[0]
                    task['Super match [# of residues]'] = superAlign[6]
                    task['Super match difference [# of residues]'] = superAlign[6] - task['Motif size [# of residues]']
            finally:
                task['SuperAlign runtime [sec]']  = clock() - task['SuperAlign runtime [sec]']
            task['CEAlign runtime [sec]']  = clock()
            try:
                ceAlign = self.cmd.cealign(querySubsetName,
                                       motifSubsetName,
                                       guide=0,
                                       window=3,
                                       transform=0)
                if ceAlign['alignment_length'] > 1:
                    task['CEAlign match [# of atoms]'] = ceAlign['alignment_length']
                    task['CEAlign RMSD [A]'] = ceAlign['RMSD']
                    task['CEAlign match difference [# of atoms]'] = task['CEAlign match [# of atoms]'] - task['Motif size [# of atoms]'] 
            finally:
                task['CEAlign runtime [sec]']  = clock() - task['CEAlign runtime [sec]']
        except BaseException as err:
            log('getRMSD: {0}'.format(err))
        finally:
            self.cmd.delete(motifSubsetName)
            self.cmd.delete(querySubsetName)
            self.cmd.delete(motifPDBCode)
            return 1       
                        
class DefaultProMolWorkflow(BaseWorkflow):
    """.. class:: DefaultProMolWorkflow(BaseWorkflow)

        The default ProMol workflow:
            (1) MotifCaller
            (2) Count / LevenshteinDistance
            (3) SuperAlign / CEAlign

        Perhaps this class should be implemented in TaskExecutor.py to cercumvent
        unorthodox import statements.

        Future work: Additional workflows are easily created by extending the existing
        *Workflow, *ComputationStep, and *Task classes, then adding the workflow
        to TaskExecutor's workflow dictionary attribute, 'workflowDict'. The desired client-side
        behavior can be implemented by extending a *JobExecutor and overriding the
        process* functions.

        Ex. 1: Automated motif generator workflow:
            1. Extend BaseTask to store motif specification data.
            2. Extend BaseComputationStep to execute Mikhail's code and store the motif
                back in the task.
            3. Extend BaseWorkflow to execute this computation step, followed by the
                DefaultProMolWorkflow for motif testing.
            4. Extend DefaultProMolJobExecutor. Override createTaskBatch to send motif
                specification data. Override processBatchResult to save the motif to the motif
                directory.

        Ex. 2: AutoDock workflow:
            1. Extend DefaultProMolTask to accomodate AutoDock results.
            2. Extend BaseComputationStep to prepare the protein/ligand in PyMOL and perform
                the AutoDock analysis in a subprocess.
            3. Extend DefaultProMolWorkflow to append AutoDockComputationStep as the fourth
                computation step in the sequence.

        etc.

    """

    def __init__(self, aminoHashTable, fetchPath):
        """.. method:: __init__(self, aminoHashTable, fetchPath)

            The DefaultProMolWorkflow is instantiated with arguments that provide access to the
            'aminoHashTable' and 'fetchPath' from promolglobals. A buried import statement
            provides access to the PyMOL API modules 'cmd' and 'stored'.
              
        """
        from pymol import cmd, stored
        BaseWorkflow.__init__(self, workflowName='DefaultProMolWorkflow',
                              computationSteps=[MotifCallerStep(aminoHashTable, cmd, stored, fetchPath),
                                                CountLevDistStep(aminoHashTable, cmd, stored),
                                                SuperCEAlignStep(aminoHashTable, cmd, stored, fetchPath)
                                                ])

class MotifTestJobExecutor(DefaultProMolJobExecutor):
    """.. class:: MotifTestJobExecutor(DefaultProMolJobExecutor)

        T

    """
    
    def __init__(self,
                 serverPort,
                 shutdownFunc,           
                 serverHost='127.0.0.1',
                 host='127.0.0.1',
                 outputDir=None):
        """.. method:: __init__(self, serverPort, shutdownFunc, serverHost='127.0.0.1', host='127.0.0.1', distributed=0)



        """
        DefaultProMolJobExecutor.__init__(self,
                                          serverPort,
                                          serverHost=serverHost,
                                          host=host,
                                          shutdownFunc=shutdownFunc,
                                          outputDir=outputDir)
        self.invalidMotifs = []

    def __call__(self, **kwargs):
        DefaultProMolJobExecutor.__call__(self, **kwargs)
        num_of_invalids = len(self.invalidMotifs)
        print 'Invalid motifs:', num_of_invalids
        if num_of_invalids > 0:
            open('invalidMotifs.txt', 'w').write('\n'.join(self.invalidMotifs))
        
    def createTaskBatches(self, motifs, motifTestSets=None, randomTestSet=None, d=0.0):
        """.. method:: createTaskBatches(self, motifs)



        """
        batchDict = {}
        for motif in motifs:
            pdb, class_ = motif.split('_',2)[1:]
            batch = [DefaultProMolTask(pdb, motif, self.resultAddr,
                                         d=d, queryClass=class_, batchName=motif).serialize()
                     ]
            if motifTestSets is not None:
                try:
                    for pdb, class_ in motifTestSets[motif]:
                        batch.append(DefaultProMolTask(pdb, motif, self.resultAddr,
                                                 d=d, queryClass=class_, batchName=motif).serialize())
                except KeyError as err:
                    print 'createTaskBatches:', err
            if randomTestSet is not None:
                for pdb, class_ in randomTestSet:
                    batch.append(DefaultProMolTask(pdb, motif, self.resultAddr,
                                                 d=d, queryClass=class_, batchName=motif).serialize())
            batchDict[motif] = batch
        return batchDict

    def processTaskResult(self, resultsStr, sock):
        """.. method:: processTaskResult(self, resultsStr, sock)

            In DefaultProMolJobExecutor, the processTaskResult method overrides the BaseJobExecutor
            method of the same name. For each task returned, some data are
            reported to STDOUT and the task is stored in the results dictionary by Query PDB ID.

            This method should by modified to merge with motif.py

        """
        for serializedTask in loads(resultsStr):
            task = BaseTask.deserialize(serializedTask)
            invalid = True
            try:
                #print task['Query PDB ID'], task['Motif'], task['Total runtime [sec]']
                #try: print task['Fetch time [sec]']
                #except: pass
                #print task['IDSpec by residue [# of residues]']
                super = False
                try: super = task['Super match difference [# of residues]'] == 0 and task['Super RMSD [A]'] < 0.1
                except Exception: pass
                ce = False
                try: ce = task['CEAlign match difference [# of atoms]'] > -6 and task['CEAlign RMSD [A]'] < 0.1
                except Exception: pass
                if super or ce:
                    invalid = False
                else:
                    print 'Invalid:', task['Motif']
            except BaseException as err: print err
            self.resultMutex.acquire()
            try: # critical region
                if invalid is True:
                    self.invalidMotifs.append(task['Motif'])
                self.result[task['batchName']].append(task)
                self.resultCount[task['batchName']] += 1
            finally: # always release the lock
                self.resultMutex.release()

class SsetCompareJobExecutor(DefaultProMolJobExecutor):
    """.. class:: SsetCompareJobExecutor(DefaultProMolJobExecutor)

        T

    """
    
    def __init__(self,
                 serverPort,
                 shutdownFunc,
                 outputDir=None,
                 serverHost='127.0.0.1',
                 host='127.0.0.1'):
        """.. method:: __init__(self, serverPort, shutdownFunc, serverHost='127.0.0.1', host='127.0.0.1', distributed=0)



        """
        DefaultProMolJobExecutor.__init__(self,
                                          serverPort,
                                          serverHost=serverHost,
                                          host=host,
                                          outputDir=outputDir,
                                          shutdownFunc=shutdownFunc)
        
    def createTaskBatches(self, motifPairs):
        """.. method:: createTaskBatches(self, motifPairs)



        """
        batchDict = {}
        for pair in motifPairs:
            batch = []
            pdb = None
            for motif in pair:
                set, pdb, class_ = motif.split('_',2)
                d = 0.0 if set is 'S' else 1.0
                batch.append(DefaultProMolTask(pdb, motif, self.resultAddr,
                                         d=d, queryClass=class_, batchName=pdb).serialize())
            batchDict[pdb] = batch
        return batchDict

    

