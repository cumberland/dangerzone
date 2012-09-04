
class moDate_Year_Season_Month_Day(Audit):
	mvDate_Year_Season_Month_Day = models.BigIntegerField(verbose_name='Orientation-1. What is the date? Year, season, month, date, day?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvDate_Year_Season_Month_Day
	class Meta:
		get_latest_by = 'record'
		


class moLocation_Country_Province_City_Hospital(Audit):
	mvLocation_Country_Province_City_Hospital = models.BigIntegerField(verbose_name='Orientation-2. Where are we? Country, province, city, name of hospital or street, floor #', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvLocation_Country_Province_City_Hospital
	class Meta:
		get_latest_by = 'record'
		


class moName3Objects_PatientRepeat(Audit):
	mvName3Objects_PatientRepeat = models.BigIntegerField(verbose_name='Registration-3. Name 3 objects (e.g. apple, penny, table) or alternates (ball, chair, tree). Then ask patient to name them Score one point for each correct answer.', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvName3Objects_PatientRepeat
	class Meta:
		get_latest_by = 'record'
		


class moRecord_Number_Of_Trials(Audit):
	mvRecord_Number_Of_Trials = models.BigIntegerField(verbose_name='Registration-NOTE: You can repeat them up to 3 times until he/she registers perfectly all 3 but base the score on the first trial. Record Number of Trials:', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvRecord_Number_Of_Trials
	class Meta:
		get_latest_by = 'record'
		


class moCount_Backwards(Audit):
	mvCount_Backwards = models.BigIntegerField(verbose_name='Attention & Calculation-4. a) Serial 7\'s. Count backwards by 7\'s from 100. Stop at five answers (100-93-86-79-72-65)', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCount_Backwards
	class Meta:
		get_latest_by = 'record'
		


class moSpell_WORLD_Backwards(Audit):
	mvSpell_WORLD_Backwards = models.BigIntegerField(verbose_name='Attention & Calculation-4. b) Ask him/her to spell "WORLD" backwards. One point for each letter in correct sequence', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvSpell_WORLD_Backwards
	class Meta:
		get_latest_by = 'record'
		


class moName_3_Objects(Audit):
	mvName_3_Objects = models.BigIntegerField(verbose_name='Recall-5. Ask for names of 3 objects given above', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvName_3_Objects
	class Meta:
		get_latest_by = 'record'
		


class moPoint_Two_Objects_NameObject(Audit):
	mvPoint_Two_Objects_NameObject = models.BigIntegerField(verbose_name='Point to two objects e.g a pencil and a watch and ask for a name. Score one point for each correct answer', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvPoint_Two_Objects_NameObject
	class Meta:
		get_latest_by = 'record'
		


class moRepeat_Phrase_NoIfsAndsButs(Audit):
	mvRepeat_Phrase_NoIfsAndsButs = models.BigIntegerField(verbose_name='LANGUAGE TESTS-Ask patient to repeat  "NO IFS ANDS OR BUTS\'.', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvRepeat_Phrase_NoIfsAndsButs
	class Meta:
		get_latest_by = 'record'
		


class moFollow_3Stage_Command(Audit):
	mvFollow_3Stage_Command = models.BigIntegerField(verbose_name='LANGUAGE TESTS-8. Ask patient to follow a 3 stage command. "TAKE THE PAPER IN YOUR RIGHT HAND, FOLD THE PAPER IN HALF ONCE AND PUT THE PAPER DOWN ON THE FLOOR".', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvFollow_3Stage_Command
	class Meta:
		get_latest_by = 'record'
		


class moRead_Phrase_Obey_Instructions(Audit):
	mvRead_Phrase_Obey_Instructions = models.BigIntegerField(verbose_name='LANGUAGE TESTS-9. Ask patient to read (CLOSE YOUR EYES) and obey the instructions.', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvRead_Phrase_Obey_Instructions
	class Meta:
		get_latest_by = 'record'
		


class moWrite_Sentence(Audit):
	mvWrite_Sentence = models.BigIntegerField(verbose_name='LANGUAGE TESTS-10. Ask patient to write sentence. Sentence must be sensible, must contain a subject and a vern and be written spontaneously. Ignore spelling errors.', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvWrite_Sentence
	class Meta:
		get_latest_by = 'record'
		


class moCopy_PentagonDiagram(Audit):
	mvCopy_PentagonDiagram = models.BigIntegerField(verbose_name='LANGUAGE TESTS-11. Show patient a diagram of intersecting pentagons and ask him/her to copy intersecting pentagons.', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCopy_PentagonDiagram
	class Meta:
		get_latest_by = 'record'
		


class moLevel_Consciousness(Audit):
	mvLevel_Consciousness = models.RadioButton(verbose_name='Level of Consciousness', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvLevel_Consciousness
	class Meta:
		get_latest_by = 'record'
		


class moEducation_Attainment(Audit):
	mvEducation_Attainment = models.CharField(verbose_name='Educational Attainment', blank=False, null=False, max_length=30)
	def __unicode__(self):
		return "%s" % self.mvEducation_Attainment
	class Meta:
		get_latest_by = 'record'
		


class moFluency_English(Audit):
	mvFluency_English = models.RadioButton(verbose_name='Fluency in English', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvFluency_English
	class Meta:
		get_latest_by = 'record'
		


class moNote_Distractibility(Audit):
	mvNote_Distractibility = models.CharField(verbose_name='Note distractibility, frustration, exhaustion, and nature of cooperation. The patient\'s impression of his/her performance should also be noted', blank=False, null=False, max_length=50)
	def __unicode__(self):
		return "%s" % self.mvNote_Distractibility
	class Meta:
		get_latest_by = 'record'
		


class moGeneral_Comments(Audit):
	mvGeneral_Comments = models.CharField(verbose_name='General Comments', blank=False, null=False, max_length=50)
	def __unicode__(self):
		return "%s" % self.mvGeneral_Comments
	class Meta:
		get_latest_by = 'record'
		


class moExaminer_Signature(Audit):
	mvExaminer_Signature = models.CharField(verbose_name='Examiner\'s Signature', blank=False, null=False, max_length=30)
	def __unicode__(self):
		return "%s" % self.mvExaminer_Signature
	class Meta:
		get_latest_by = 'record'
		


class moExaminer_Signature_DateTime(Audit):
	mvExaminer_Signature_DateTime = models.DateTimeField(verbose_name='Examiner\' Signature-Date and Time', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvExaminer_Signature_DateTime
	class Meta:
		get_latest_by = 'record'
		


class moVisuospatialExecutive(Audit):
	mvVisuospatialExecutive = models.BigIntegerField(verbose_name='Visuospatial/Executive', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvVisuospatialExecutive
	class Meta:
		get_latest_by = 'record'
		


class moVisuospatialExecutive_CopyCube(Audit):
	mvVisuospatialExecutive_CopyCube = models.BigIntegerField(verbose_name='Visuospatial/Executive-Copy Cube', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvVisuospatialExecutive_CopyCube
	class Meta:
		get_latest_by = 'record'
		


class moVisuoExecutive_DrawClock_Contour(Audit):
	mvVisuoExecutive_DrawClock_Contour = models.BigIntegerField(verbose_name='Visuospatial/Executive-Draw CLOCK-Contour', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvVisuoExecutive_DrawClock_Contour
	class Meta:
		get_latest_by = 'record'
		


class moVisuoExecutive_DrawClock_Numbers(Audit):
	mvVisuoExecutive_DrawClock_Numbers = models.BigIntegerField(verbose_name='Visuospatial/Executive-Draw CLOCK-Numbers', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvVisuoExecutive_DrawClock_Numbers
	class Meta:
		get_latest_by = 'record'
		


class moVisuoExecutive_DrawClock_Hands(Audit):
	mvVisuoExecutive_DrawClock_Hands = models.BigIntegerField(verbose_name='Visuospatial/Executive-Draw CLOCK-Hands', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvVisuoExecutive_DrawClock_Hands
	class Meta:
		get_latest_by = 'record'
		


class moNaming_Lion(Audit):
	mvNaming_Lion = models.BigIntegerField(verbose_name='Naming-Lion', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvNaming_Lion
	class Meta:
		get_latest_by = 'record'
		


class moNaming_Rhinocerous(Audit):
	mvNaming_Rhinocerous = models.BigIntegerField(verbose_name='Naming-Rhinocerous', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvNaming_Rhinocerous
	class Meta:
		get_latest_by = 'record'
		


class moNaming_Camel(Audit):
	mvNaming_Camel = models.BigIntegerField(verbose_name='Naming-Camel', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvNaming_Camel
	class Meta:
		get_latest_by = 'record'
		


class moMemory_1stTrial_Face(Audit):
	mvMemory_1stTrial_Face = models.BigIntegerField(verbose_name='Memory 1st trial Face', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvMemory_1stTrial_Face
	class Meta:
		get_latest_by = 'record'
		


class moMemory_1stTrial_Velvet(Audit):
	mvMemory_1stTrial_Velvet = models.BigIntegerField(verbose_name='MEMORY-1st trial-Velvet', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvMemory_1stTrial_Velvet
	class Meta:
		get_latest_by = 'record'
		


class moMemory_1stTrial_Church(Audit):
	mvMemory_1stTrial_Church = models.BigIntegerField(verbose_name='MEMORY-1st trial-CHURCH', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvMemory_1stTrial_Church
	class Meta:
		get_latest_by = 'record'
		


class moMemory_1stTrial_Daisy(Audit):
	mvMemory_1stTrial_Daisy = models.BigIntegerField(verbose_name='MEMORY-1st trial-Daisy', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvMemory_1stTrial_Daisy
	class Meta:
		get_latest_by = 'record'
		


class moMemory_1stTrial_Red(Audit):
	mvMemory_1stTrial_Red = models.BigIntegerField(verbose_name='MEMORY-1st trial-Red', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvMemory_1stTrial_Red
	class Meta:
		get_latest_by = 'record'
		


class moMemory_2ndTrial_Face(Audit):
	mvMemory_2ndTrial_Face = models.BigIntegerField(verbose_name='MEMORY-2nd trial-Face', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvMemory_2ndTrial_Face
	class Meta:
		get_latest_by = 'record'
		


class moMemory_2ndTrial_Velvet(Audit):
	mvMemory_2ndTrial_Velvet = models.BigIntegerField(verbose_name='MEMORY-2nd trial-Velvet', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvMemory_2ndTrial_Velvet
	class Meta:
		get_latest_by = 'record'
		


class moMemory_2ndTrial_Church(Audit):
	mvMemory_2ndTrial_Church = models.BigIntegerField(verbose_name='MEMORY-2nd trial-Church', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvMemory_2ndTrial_Church
	class Meta:
		get_latest_by = 'record'
		


class moMemory_2ndTrial_Daisy(Audit):
	mvMemory_2ndTrial_Daisy = models.BigIntegerField(verbose_name='MEMORY-2nd trial-Daisy', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvMemory_2ndTrial_Daisy
	class Meta:
		get_latest_by = 'record'
		


class moMemory_2ndTrial_Red(Audit):
	mvMemory_2ndTrial_Red = models.BigIntegerField(verbose_name='MEMORY-2nd trial-Red', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvMemory_2ndTrial_Red
	class Meta:
		get_latest_by = 'record'
		


class moAttention_RepeatForward_21854(Audit):
	mvAttention_RepeatForward_21854 = models.BigIntegerField(verbose_name='ATTENTION-Repeat list of digits in the forward order 21854', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvAttention_RepeatForward_21854
	class Meta:
		get_latest_by = 'record'
		


class moAttention_RepeatBackward_742(Audit):
	mvAttention_RepeatBackward_742 = models.BigIntegerField(verbose_name='ATTENTION-Repeat list of digits in the backward order 742', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvAttention_RepeatBackward_742
	class Meta:
		get_latest_by = 'record'
		


class moAttention_Read_List_Letters(Audit):
	mvAttention_Read_List_Letters = models.BigIntegerField(verbose_name='ATTENTION-Read List of Letters FBACMNAAJKLBAFAKDEAAAJAMOFAAB', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvAttention_Read_List_Letters
	class Meta:
		get_latest_by = 'record'
		


class moAttention_Serial7Subtract_93(Audit):
	mvAttention_Serial7Subtract_93 = models.BigIntegerField(verbose_name='ATTENTION-Serial 7 Subtraction Starting at 100-93', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvAttention_Serial7Subtract_93
	class Meta:
		get_latest_by = 'record'
		


class moAttention_Serial7Subtract_86(Audit):
	mvAttention_Serial7Subtract_86 = models.BigIntegerField(verbose_name='ATTENTION-Serial 7 Subtraction Starting at 100-86', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvAttention_Serial7Subtract_86
	class Meta:
		get_latest_by = 'record'
		


class moAttention_Serial7Subtract_79(Audit):
	mvAttention_Serial7Subtract_79 = models.BigIntegerField(verbose_name='ATTENTION-Serial 7 Subtraction Starting at 100-79', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvAttention_Serial7Subtract_79
	class Meta:
		get_latest_by = 'record'
		


class moAttention_Serial7Subtract_65(Audit):
	mvAttention_Serial7Subtract_65 = models.BigIntegerField(verbose_name='ATTENTION-Serial 7 Subtraction Starting at 100-65', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvAttention_Serial7Subtract_65
	class Meta:
		get_latest_by = 'record'
		


class moLanguage_Repeat(Audit):
	mvLanguage_Repeat = models.BigIntegerField(verbose_name='LANGUAGE-Repeat "I only know that John is the one to help today"', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvLanguage_Repeat
	class Meta:
		get_latest_by = 'record'
		


class moLanguage_Repeat_Phrase2(Audit):
	mvLanguage_Repeat_Phrase2 = models.BigIntegerField(verbose_name='LANGUAGE-Repeat "The cat always hid under the couch when the dogs were in the room"', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvLanguage_Repeat_Phrase2
	class Meta:
		get_latest_by = 'record'
		


class moAbstraction_TrainBicycle(Audit):
	mvAbstraction_TrainBicycle = models.BigIntegerField(verbose_name='ABSTRACTION-Train-bicycle', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvAbstraction_TrainBicycle
	class Meta:
		get_latest_by = 'record'
		


class moAbstraction_WatchRuler(Audit):
	mvAbstraction_WatchRuler = models.BigIntegerField(verbose_name='ABSTRACTION-Watch-Ruler', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvAbstraction_WatchRuler
	class Meta:
		get_latest_by = 'record'
		


class moDelayedRecall_NoCue_Face(Audit):
	mvDelayedRecall_NoCue_Face = models.BigIntegerField(verbose_name='DELAYED RECALL-No Cue-Face', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvDelayedRecall_NoCue_Face
	class Meta:
		get_latest_by = 'record'
		


class moDelayedRecall_NoCue_Velvet(Audit):
	mvDelayedRecall_NoCue_Velvet = models.BigIntegerField(verbose_name='DELAYED RECALL-No Cue-Velvet', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvDelayedRecall_NoCue_Velvet
	class Meta:
		get_latest_by = 'record'
		


class moDelayedRecall_NoCue_Church(Audit):
	mvDelayedRecall_NoCue_Church = models.BigIntegerField(verbose_name='DELAYED RECALL-No Cue-Church', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvDelayedRecall_NoCue_Church
	class Meta:
		get_latest_by = 'record'
		


class moDelayedRecall_NoCue_Daisy(Audit):
	mvDelayedRecall_NoCue_Daisy = models.BigIntegerField(verbose_name='DELAYED RECALL-No Cue-Daisy', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvDelayedRecall_NoCue_Daisy
	class Meta:
		get_latest_by = 'record'
		


class moOrientation_Date(Audit):
	mvOrientation_Date = models.BigIntegerField(verbose_name='ORIENTATION-Date', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvOrientation_Date
	class Meta:
		get_latest_by = 'record'
		


class moOrientation_Month(Audit):
	mvOrientation_Month = models.BigIntegerField(verbose_name='ORIENTATION-Month', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvOrientation_Month
	class Meta:
		get_latest_by = 'record'
		


class moOrientation_Year(Audit):
	mvOrientation_Year = models.BigIntegerField(verbose_name='ORIENTATION-Year', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvOrientation_Year
	class Meta:
		get_latest_by = 'record'
		


class moOrientation_Day(Audit):
	mvOrientation_Day = models.BigIntegerField(verbose_name='ORIENTATION-Day', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvOrientation_Day
	class Meta:
		get_latest_by = 'record'
		


class moOrientation_Place(Audit):
	mvOrientation_Place = models.BigIntegerField(verbose_name='ORIENTATION-Place', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvOrientation_Place
	class Meta:
		get_latest_by = 'record'
		


class moOrientation_City(Audit):
	mvOrientation_City = models.BigIntegerField(verbose_name='ORIENTATION-City', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvOrientation_City
	class Meta:
		get_latest_by = 'record'
		


class moCERAD_Name(Audit):
	mvCERAD_Name = models.CharField(verbose_name='CERAD-Name', blank=False, null=False, max_length=30)
	def __unicode__(self):
		return "%s" % self.mvCERAD_Name
	class Meta:
		get_latest_by = 'record'
		


class moCERAD_NIS(Audit):
	mvCERAD_NIS = models.CharField(verbose_name='CERAD-NIS', blank=False, null=False, max_length=30)
	def __unicode__(self):
		return "%s" % self.mvCERAD_NIS
	class Meta:
		get_latest_by = 'record'
		


class moCERAD_date(Audit):
	mvCERAD_date = models.DateField(verbose_name='CERAD-Date', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCERAD_date
	class Meta:
		get_latest_by = 'record'
		


class moCERAD_MiniMentalState(Audit):
	mvCERAD_MiniMentalState = models.BigIntegerField(verbose_name='CERAD-Mini Mental State', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCERAD_MiniMentalState
	class Meta:
		get_latest_by = 'record'
		


class moCERAD_VerbalFluency(Audit):
	mvCERAD_VerbalFluency = models.BigIntegerField(verbose_name='CERAD-Verbal Fluency', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCERAD_VerbalFluency
	class Meta:
		get_latest_by = 'record'
		


class moCERAD_BostonNamingTest(Audit):
	mvCERAD_BostonNamingTest = models.BigIntegerField(verbose_name='CERAD_Boston Naming Test', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCERAD_BostonNamingTest
	class Meta:
		get_latest_by = 'record'
		


class moCERAD_WordListMemory_Trial(Audit):
	mvCERAD_WordListMemory_Trial = models.RadioButton(verbose_name='CERAD_Word List Memory-Trial', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCERAD_WordListMemory_Trial
	class Meta:
		get_latest_by = 'record'
		


class moCERAD_WordListMemory(Audit):
	mvCERAD_WordListMemory = models.BigIntegerField(verbose_name='CERAD_Word List Memory', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCERAD_WordListMemory
	class Meta:
		get_latest_by = 'record'
		


class moCERAD_Intrustions(Audit):
	mvCERAD_Intrustions = models.BigIntegerField(verbose_name='CERAD_Intrusions', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvCERAD_Intrustions
	class Meta:
		get_latest_by = 'record'
		


class moCERAD_ConstructionalPraxis(Audit):
	mvCERAD_ConstructionalPraxis = models.BigIntegerField(verbose_name='CERAD-Constructional Praxis', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCERAD_ConstructionalPraxis
	class Meta:
		get_latest_by = 'record'
		


class moCERAD_WordListRecall(Audit):
	mvCERAD_WordListRecall = models.BigIntegerField(verbose_name='CERAD-Word List Recall', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCERAD_WordListRecall
	class Meta:
		get_latest_by = 'record'
		


class moCERAD_intrusions(Audit):
	mvCERAD_intrusions = models.BigIntegerField(verbose_name='CERAD-Intrusions', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvCERAD_intrusions
	class Meta:
		get_latest_by = 'record'
		


class moCERAD_WordListRecognition(Audit):
	mvCERAD_WordListRecognition = models.BigIntegerField(verbose_name='CERAD-Word List Recognition', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCERAD_WordListRecognition
	class Meta:
		get_latest_by = 'record'
		


class moVerbFluency_NIS(Audit):
	mvVerbFluency_NIS = models.CharField(verbose_name='Verbal Fluency Categories-NIS', blank=False, null=False, max_length=30)
	def __unicode__(self):
		return "%s" % self.mvVerbFluency_NIS
	class Meta:
		get_latest_by = 'record'
		


class moVerbFluency_Visit(Audit):
	mvVerbFluency_Visit = models.BigIntegerField(verbose_name='Verbal Fluency Categories-Visit', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvVerbFluency_Visit
	class Meta:
		get_latest_by = 'record'
		


class moVerbFluency_Date(Audit):
	mvVerbFluency_Date = models.DateField(verbose_name='Verbal Fluency Categories-Date', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvVerbFluency_Date
	class Meta:
		get_latest_by = 'record'
		


class moVerbFluency_ExaminerInit(Audit):
	mvVerbFluency_ExaminerInit = models.CharField(verbose_name='Verbal Fluency Categories-Examiner\'s Initials', blank=False, null=False, max_length=3)
	def __unicode__(self):
		return "%s" % self.mvVerbFluency_ExaminerInit
	class Meta:
		get_latest_by = 'record'
		


class moWordCount_015Seconds(Audit):
	mvWordCount_015Seconds = models.BigIntegerField(verbose_name='Word Count-16-30', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvWordCount_015Seconds
	class Meta:
		get_latest_by = 'record'
		


class moWordCount_1630Seconds(Audit):
	mvWordCount_1630Seconds = models.BigIntegerField(verbose_name='Word Count-16-30', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvWordCount_1630Seconds
	class Meta:
		get_latest_by = 'record'
		


class moWordCount_3145Seconds(Audit):
	mvWordCount_3145Seconds = models.BigIntegerField(verbose_name='Word Count-31-45 seconds', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvWordCount_3145Seconds
	class Meta:
		get_latest_by = 'record'
		


class moWordCount_4660Seconds(Audit):
	mvWordCount_4660Seconds = models.BigIntegerField(verbose_name='Word Count-46-60 seconds', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvWordCount_4660Seconds
	class Meta:
		get_latest_by = 'record'
		


class moBNT_High_Tree(Audit):
	mvBNT_High_Tree = models.BigIntegerField(verbose_name='BNT-HIGH-Tree', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvBNT_High_Tree
	class Meta:
		get_latest_by = 'record'
		


class moBNT_High_Bed(Audit):
	mvBNT_High_Bed = models.BigIntegerField(verbose_name='BNT-HIGH-Bed', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvBNT_High_Bed
	class Meta:
		get_latest_by = 'record'
		


class moBNT_High_Whistle(Audit):
	mvBNT_High_Whistle = models.BigIntegerField(verbose_name='BNT-HIGH-Whistle', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvBNT_High_Whistle
	class Meta:
		get_latest_by = 'record'
		


class moBNT_High_Flower(Audit):
	mvBNT_High_Flower = models.BigIntegerField(verbose_name='BNT-HIGH-Flower', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvBNT_High_Flower
	class Meta:
		get_latest_by = 'record'
		


class moBNT_High_House(Audit):
	mvBNT_High_House = models.BigIntegerField(verbose_name='BNT-HIGH-House', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvBNT_High_House
	class Meta:
		get_latest_by = 'record'
		


class moBNT_Medium_Canoe(Audit):
	mvBNT_Medium_Canoe = models.BigIntegerField(verbose_name='BNT-Medium-Canoe', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvBNT_Medium_Canoe
	class Meta:
		get_latest_by = 'record'
		


class moBNT_Medium_ToothBrush(Audit):
	mvBNT_Medium_ToothBrush = models.BigIntegerField(verbose_name='BNT-MEDIUM-Tooth Brush', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvBNT_Medium_ToothBrush
	class Meta:
		get_latest_by = 'record'
		


class moBNT_Medium_Vocano(Audit):
	mvBNT_Medium_Vocano = models.BigIntegerField(verbose_name='BNT-MEDIUM-Volcano', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvBNT_Medium_Vocano
	class Meta:
		get_latest_by = 'record'
		


class moBNT_Medium_Mask(Audit):
	mvBNT_Medium_Mask = models.BigIntegerField(verbose_name='BNT-MEDIUM-Mask', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvBNT_Medium_Mask
	class Meta:
		get_latest_by = 'record'
		


class moBNT_Medium_Camel(Audit):
	mvBNT_Medium_Camel = models.BigIntegerField(verbose_name='BNT-MEDIUM-Camel', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvBNT_Medium_Camel
	class Meta:
		get_latest_by = 'record'
		


class moBNT_Low_Harmonica(Audit):
	mvBNT_Low_Harmonica = models.BigIntegerField(verbose_name='BNT-LOW-Harmonica', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvBNT_Low_Harmonica
	class Meta:
		get_latest_by = 'record'
		


class moBNT_Low_Tongs(Audit):
	mvBNT_Low_Tongs = models.BigIntegerField(verbose_name='BNT-LOW-Tongs', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvBNT_Low_Tongs
	class Meta:
		get_latest_by = 'record'
		


class moBNT_Low_Hammock(Audit):
	mvBNT_Low_Hammock = models.BigIntegerField(verbose_name='BNT-LOW-Hammock', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvBNT_Low_Hammock
	class Meta:
		get_latest_by = 'record'
		


class moBNT_Low_Funnel(Audit):
	mvBNT_Low_Funnel = models.BigIntegerField(verbose_name='BNT-LOW-Funnel', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvBNT_Low_Funnel
	class Meta:
		get_latest_by = 'record'
		


class moBNT_Low_Dominoes(Audit):
	mvBNT_Low_Dominoes = models.BigIntegerField(verbose_name='BNT-LOW-Dominoes', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvBNT_Low_Dominoes
	class Meta:
		get_latest_by = 'record'
		


class moBNT_PicCorrect_High(Audit):
	mvBNT_PicCorrect_High = models.BigIntegerField(verbose_name='BNT-Picture Correct-HIGH', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvBNT_PicCorrect_High
	class Meta:
		get_latest_by = 'record'
		


class moBNT_PicCorrect_Medium(Audit):
	mvBNT_PicCorrect_Medium = models.BigIntegerField(verbose_name='BNT-Picture Correct-MEDIUM', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvBNT_PicCorrect_Medium
	class Meta:
		get_latest_by = 'record'
		


class moBNT_PicCorrect_Low(Audit):
	mvBNT_PicCorrect_Low = models.BigIntegerField(verbose_name='BNT-Picture Correct-LOW', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvBNT_PicCorrect_Low
	class Meta:
		get_latest_by = 'record'
		


class moBNT_PicCorrect_Total(Audit):
	mvBNT_PicCorrect_Total = models.BigIntegerField(verbose_name='BNT_Picture Correct-TOTAL', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvBNT_PicCorrect_Total
	class Meta:
		get_latest_by = 'record'
		


class moWLMT_Trial1_Butter(Audit):
	mvWLMT_Trial1_Butter = models.BooleanField(verbose_name='WLMT-TRIAL 1-Butter')
	def __unicode__(self):
		return "%s" % self.mvWLMT_Trial1_Butter
	class Meta:
		get_latest_by = 'record'
		


class moWLMT_Trial1_Arm(Audit):
	mvWLMT_Trial1_Arm = models.BooleanField(verbose_name='WLMT-TRIAL 1-Arm')
	def __unicode__(self):
		return "%s" % self.mvWLMT_Trial1_Arm
	class Meta:
		get_latest_by = 'record'
		


class moWLMT_Trial1_Shore(Audit):
	mvWLMT_Trial1_Shore = models.BooleanField(verbose_name='WLMT-TRIAL 1-Shore')
	def __unicode__(self):
		return "%s" % self.mvWLMT_Trial1_Shore
	class Meta:
		get_latest_by = 'record'
		


class moWLMT_Trial1_Letter(Audit):
	mvWLMT_Trial1_Letter = models.BooleanField(verbose_name='WLMT-TRIAL 1-Letter')
	def __unicode__(self):
		return "%s" % self.mvWLMT_Trial1_Letter
	class Meta:
		get_latest_by = 'record'
		


class moWLMT_Trial1_Queen(Audit):
	mvWLMT_Trial1_Queen = models.BooleanField(verbose_name='WLMT-TRIAL 1-Queen')
	def __unicode__(self):
		return "%s" % self.mvWLMT_Trial1_Queen
	class Meta:
		get_latest_by = 'record'
		


class moWLMT_Trial1_Cabin(Audit):
	mvWLMT_Trial1_Cabin = models.BooleanField(verbose_name='WLMT-TRIAL 1-Cabin')
	def __unicode__(self):
		return "%s" % self.mvWLMT_Trial1_Cabin
	class Meta:
		get_latest_by = 'record'
		


class moWLMT_Trial1_Pole(Audit):
	mvWLMT_Trial1_Pole = models.BooleanField(verbose_name='WLMT-TRIAL 1-Pole')
	def __unicode__(self):
		return "%s" % self.mvWLMT_Trial1_Pole
	class Meta:
		get_latest_by = 'record'
		


class moWLMT_Trial1_Ticket(Audit):
	mvWLMT_Trial1_Ticket = models.BooleanField(verbose_name='WLMT-TRIAL 1-Ticket')
	def __unicode__(self):
		return "%s" % self.mvWLMT_Trial1_Ticket
	class Meta:
		get_latest_by = 'record'
		


class moWLMT_Trial1_Grass(Audit):
	mvWLMT_Trial1_Grass = models.BooleanField(verbose_name='WLMT-TRIAL 1-Grass')
	def __unicode__(self):
		return "%s" % self.mvWLMT_Trial1_Grass
	class Meta:
		get_latest_by = 'record'
		


class moWLMT_TRIAL2_Ticket(Audit):
	mvWLMT_TRIAL2_Ticket = models.BooleanField(verbose_name='WLMT-TRIAL 2-Ticket')
	def __unicode__(self):
		return "%s" % self.mvWLMT_TRIAL2_Ticket
	class Meta:
		get_latest_by = 'record'
		


class moWLMT_TRIAL2_Cabin(Audit):
	mvWLMT_TRIAL2_Cabin = models.BooleanField(verbose_name='WLMT-TRIAL 2-Cabin')
	def __unicode__(self):
		return "%s" % self.mvWLMT_TRIAL2_Cabin
	class Meta:
		get_latest_by = 'record'
		


class moWLMT_TRIAL2_Butter(Audit):
	mvWLMT_TRIAL2_Butter = models.BooleanField(verbose_name='WLMT-TRIAL 2-Butter')
	def __unicode__(self):
		return "%s" % self.mvWLMT_TRIAL2_Butter
	class Meta:
		get_latest_by = 'record'
		


class moWLMT_Trial2_Shore(Audit):
	mvWLMT_Trial2_Shore = models.BooleanField(verbose_name='WLMT-TRIAL 2-Shore')
	def __unicode__(self):
		return "%s" % self.mvWLMT_Trial2_Shore
	class Meta:
		get_latest_by = 'record'
		


class moWLMT_Trial2_Engine(Audit):
	mvWLMT_Trial2_Engine = models.BooleanField(verbose_name='WLMT-TRIAL 2-Engine')
	def __unicode__(self):
		return "%s" % self.mvWLMT_Trial2_Engine
	class Meta:
		get_latest_by = 'record'
		


class moWLMT_Trial2_Arm(Audit):
	mvWLMT_Trial2_Arm = models.BooleanField(verbose_name='WLMT-TRIAL 2-Arm')
	def __unicode__(self):
		return "%s" % self.mvWLMT_Trial2_Arm
	class Meta:
		get_latest_by = 'record'
		


class moWLMT_Trial2_Queen(Audit):
	mvWLMT_Trial2_Queen = models.BooleanField(verbose_name='WLMT-TRIAL 2-Queen')
	def __unicode__(self):
		return "%s" % self.mvWLMT_Trial2_Queen
	class Meta:
		get_latest_by = 'record'
		


class moWLMT_Trial2_Letter(Audit):
	mvWLMT_Trial2_Letter = models.BooleanField(verbose_name='WLMT-TRIAL 2-Letter')
	def __unicode__(self):
		return "%s" % self.mvWLMT_Trial2_Letter
	class Meta:
		get_latest_by = 'record'
		


class moWLMT_Trial2_Grass(Audit):
	mvWLMT_Trial2_Grass = models.BooleanField(verbose_name='WLMT-TRIAL 2-Grass')
	def __unicode__(self):
		return "%s" % self.mvWLMT_Trial2_Grass
	class Meta:
		get_latest_by = 'record'
		


class moWLMT_Trial3_Queen(Audit):
	mvWLMT_Trial3_Queen = models.BooleanField(verbose_name='WLMT_TRIAL3_Queen')
	def __unicode__(self):
		return "%s" % self.mvWLMT_Trial3_Queen
	class Meta:
		get_latest_by = 'record'
		


class moWLMT_Trial3_Grass(Audit):
	mvWLMT_Trial3_Grass = models.BooleanField(verbose_name='WLMT_TRIAL3_Grass')
	def __unicode__(self):
		return "%s" % self.mvWLMT_Trial3_Grass
	class Meta:
		get_latest_by = 'record'
		


class moWLMT_Trial3_Arm(Audit):
	mvWLMT_Trial3_Arm = models.BooleanField(verbose_name='WLMT_Trial3_Arm')
	def __unicode__(self):
		return "%s" % self.mvWLMT_Trial3_Arm
	class Meta:
		get_latest_by = 'record'
		


class moWLMT_TRIAL3_Cabin(Audit):
	mvWLMT_TRIAL3_Cabin = models.BooleanField(verbose_name='WLMT-TRIAL 3-Cabin')
	def __unicode__(self):
		return "%s" % self.mvWLMT_TRIAL3_Cabin
	class Meta:
		get_latest_by = 'record'
		


class moWLMT_Trial3_Pole(Audit):
	mvWLMT_Trial3_Pole = models.BooleanField(verbose_name='WLMT-TRIAL 3-Pole')
	def __unicode__(self):
		return "%s" % self.mvWLMT_Trial3_Pole
	class Meta:
		get_latest_by = 'record'
		


class moWLMT_Trial3_Shore(Audit):
	mvWLMT_Trial3_Shore = models.BooleanField(verbose_name='WLMT-TRIAL 3-Shore')
	def __unicode__(self):
		return "%s" % self.mvWLMT_Trial3_Shore
	class Meta:
		get_latest_by = 'record'
		


class moWLMT_Trial3_Butter(Audit):
	mvWLMT_Trial3_Butter = models.BooleanField(verbose_name='WLMT-TRIAL 3-Butter')
	def __unicode__(self):
		return "%s" % self.mvWLMT_Trial3_Butter
	class Meta:
		get_latest_by = 'record'
		


class moWLMT_Trial3_Engine(Audit):
	mvWLMT_Trial3_Engine = models.BooleanField(verbose_name='WLMT-TRIAL 3-Engine')
	def __unicode__(self):
		return "%s" % self.mvWLMT_Trial3_Engine
	class Meta:
		get_latest_by = 'record'
		


class moWLMT_Trial3_Ticket(Audit):
	mvWLMT_Trial3_Ticket = models.BooleanField(verbose_name='WLMT-TRIAL 3-Ticket')
	def __unicode__(self):
		return "%s" % self.mvWLMT_Trial3_Ticket
	class Meta:
		get_latest_by = 'record'
		


class moWLMT_Trial3_Letter(Audit):
	mvWLMT_Trial3_Letter = models.BooleanField(verbose_name='WLMT-TRIAL 3-Letter')
	def __unicode__(self):
		return "%s" % self.mvWLMT_Trial3_Letter
	class Meta:
		get_latest_by = 'record'
		


class moWLMT_Trial1_Correct(Audit):
	mvWLMT_Trial1_Correct = models.BigIntegerField(verbose_name='WLMT-Trial 1-Correct', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvWLMT_Trial1_Correct
	class Meta:
		get_latest_by = 'record'
		


class moWLMT_Trial2_Correct(Audit):
	mvWLMT_Trial2_Correct = models.BigIntegerField(verbose_name='WLMT-Trial 2-Correct', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvWLMT_Trial2_Correct
	class Meta:
		get_latest_by = 'record'
		


class moWLMT_Trial3_Correct(Audit):
	mvWLMT_Trial3_Correct = models.BigIntegerField(verbose_name='WLMT-Trial 3-Correct', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvWLMT_Trial3_Correct
	class Meta:
		get_latest_by = 'record'
		


class moWLMT_Trial1_Intrusions(Audit):
	mvWLMT_Trial1_Intrusions = models.BigIntegerField(verbose_name='WLMT-Trial 1-Intrusions', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvWLMT_Trial1_Intrusions
	class Meta:
		get_latest_by = 'record'
		


class moWLMT_Trial2_Intrusions(Audit):
	mvWLMT_Trial2_Intrusions = models.BigIntegerField(verbose_name='WLMT-Trial 2-Intrusions', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvWLMT_Trial2_Intrusions
	class Meta:
		get_latest_by = 'record'
		


class moWLMT_Trial3_Intrusions(Audit):
	mvWLMT_Trial3_Intrusions = models.BigIntegerField(verbose_name='WLMT-Trial 3-Intrusions', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvWLMT_Trial3_Intrusions
	class Meta:
		get_latest_by = 'record'
		


class moWLMT_NIS(Audit):
	mvWLMT_NIS = models.CharField(verbose_name='WLMT-NIS', blank=False, null=False, max_length=30)
	def __unicode__(self):
		return "%s" % self.mvWLMT_NIS
	class Meta:
		get_latest_by = 'record'
		


class moCP_NIS(Audit):
	mvCP_NIS = models.CharField(verbose_name='CP-NIS', blank=False, null=False, max_length=30)
	def __unicode__(self):
		return "%s" % self.mvCP_NIS
	class Meta:
		get_latest_by = 'record'
		


class moCP_Visit(Audit):
	mvCP_Visit = models.BigIntegerField(verbose_name='CP_Visit', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCP_Visit
	class Meta:
		get_latest_by = 'record'
		


class moCP_Date(Audit):
	mvCP_Date = models.DateField(verbose_name='CP-Date', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCP_Date
	class Meta:
		get_latest_by = 'record'
		


class moCP_Item1_ClosedCircle(Audit):
	mvCP_Item1_ClosedCircle = models.RadioButton(verbose_name='CP-Item 1-Circle a) Closed Circle', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCP_Item1_ClosedCircle
	class Meta:
		get_latest_by = 'record'
		


class moCP_Item1_CircularShape(Audit):
	mvCP_Item1_CircularShape = models.RadioButton(verbose_name='CP-Item 1-Circle b) Circular Shape', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCP_Item1_CircularShape
	class Meta:
		get_latest_by = 'record'
		


class moCP_Item2Diamond_Draw4Sides(Audit):
	mvCP_Item2Diamond_Draw4Sides = models.RadioButton(verbose_name='CP-Item 2-Diamond a) Draws 4 sides', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCP_Item2Diamond_Draw4Sides
	class Meta:
		get_latest_by = 'record'
		


class moCP_Item2Diamond_Closes4Angles(Audit):
	mvCP_Item2Diamond_Closes4Angles = models.RadioButton(verbose_name='CP-Item 2-Diamond b) Closes all 4 angles of figure', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCP_Item2Diamond_Closes4Angles
	class Meta:
		get_latest_by = 'record'
		


class moCP_Item1Diamond_SidesEqualLength(Audit):
	mvCP_Item1Diamond_SidesEqualLength = models.RadioButton(verbose_name='CP-Item 1-Diamond c) Sides of approximately equal length', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCP_Item1Diamond_SidesEqualLength
	class Meta:
		get_latest_by = 'record'
		


class moCP_Item3Rectangle_FourSided(Audit):
	mvCP_Item3Rectangle_FourSided = models.RadioButton(verbose_name='CP-Item 3-Rectangles a) Figures are 4 sided', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCP_Item3Rectangle_FourSided
	class Meta:
		get_latest_by = 'record'
		


class moCP_Item3Rectangles_Overlap(Audit):
	mvCP_Item3Rectangles_Overlap = models.RadioButton(verbose_name='CP-Item 3-Rectangles b) Overlap resembles original', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCP_Item3Rectangles_Overlap
	class Meta:
		get_latest_by = 'record'
		


class moCP_Item4Cube_3D(Audit):
	mvCP_Item4Cube_3D = models.RadioButton(verbose_name='CP-Item 4-Cube a) Figure is 3-dimensional', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCP_Item4Cube_3D
	class Meta:
		get_latest_by = 'record'
		


class moCP_Item4Cube_FrontFaceOrientation(Audit):
	mvCP_Item4Cube_FrontFaceOrientation = models.RadioButton(verbose_name='CP-Item 4-Cube b) Frontal face correctly oriented', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCP_Item4Cube_FrontFaceOrientation
	class Meta:
		get_latest_by = 'record'
		


class moCP_Item4Cube_InternalLines(Audit):
	mvCP_Item4Cube_InternalLines = models.RadioButton(verbose_name='CP-Item 4-Cube c) Internal lines correctly drawn', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCP_Item4Cube_InternalLines
	class Meta:
		get_latest_by = 'record'
		


class moCP_Item4Cube_SidesParallel(Audit):
	mvCP_Item4Cube_SidesParallel = models.RadioButton(verbose_name='CP-Item 4-Cube d) Opposite sides are parallel (within 10 degrees)', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCP_Item4Cube_SidesParallel
	class Meta:
		get_latest_by = 'record'
		


class moCP_Total_Item1(Audit):
	mvCP_Total_Item1 = models.BigIntegerField(verbose_name='CP-TOTAL-Item 1', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvCP_Total_Item1
	class Meta:
		get_latest_by = 'record'
		


class moCP_Total_Item2(Audit):
	mvCP_Total_Item2 = models.BigIntegerField(verbose_name='CP-TOTAL-Item 2', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvCP_Total_Item2
	class Meta:
		get_latest_by = 'record'
		


class moCP_Total_Item3(Audit):
	mvCP_Total_Item3 = models.BigIntegerField(verbose_name='CP-TOTAL-Item 3', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvCP_Total_Item3
	class Meta:
		get_latest_by = 'record'
		


class moCP_Total_Item4(Audit):
	mvCP_Total_Item4 = models.BigIntegerField(verbose_name='CP-TOTAL-Item 4', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvCP_Total_Item4
	class Meta:
		get_latest_by = 'record'
		


class moWLR_Church(Audit):
	mvWLR_Church = models.BigIntegerField(verbose_name='WLR-Church', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvWLR_Church
	class Meta:
		get_latest_by = 'record'
		


class moWLR_Coffee(Audit):
	mvWLR_Coffee = models.BigIntegerField(verbose_name='WLR-Coffee', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvWLR_Coffee
	class Meta:
		get_latest_by = 'record'
		


class moWLR_Butter(Audit):
	mvWLR_Butter = models.BigIntegerField(verbose_name='WLR-Butter', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvWLR_Butter
	class Meta:
		get_latest_by = 'record'
		


class moWLR_Dollar(Audit):
	mvWLR_Dollar = models.BigIntegerField(verbose_name='WLR-Dollar', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvWLR_Dollar
	class Meta:
		get_latest_by = 'record'
		


class moWLR_Arm(Audit):
	mvWLR_Arm = models.BigIntegerField(verbose_name='WLR-Arm', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvWLR_Arm
	class Meta:
		get_latest_by = 'record'
		


class moWLR_Shore(Audit):
	mvWLR_Shore = models.BigIntegerField(verbose_name='WLR-Shore', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvWLR_Shore
	class Meta:
		get_latest_by = 'record'
		


class moWLR_Five(Audit):
	mvWLR_Five = models.BigIntegerField(verbose_name='WLR-Five', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvWLR_Five
	class Meta:
		get_latest_by = 'record'
		


class moWLR_Letter(Audit):
	mvWLR_Letter = models.BigIntegerField(verbose_name='WLR-Letter', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvWLR_Letter
	class Meta:
		get_latest_by = 'record'
		


class moWLR_Hotel(Audit):
	mvWLR_Hotel = models.BigIntegerField(verbose_name='WLR-Hotel', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvWLR_Hotel
	class Meta:
		get_latest_by = 'record'
		


class moWLR_Mountain(Audit):
	mvWLR_Mountain = models.BigIntegerField(verbose_name='WLR-Mountain', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvWLR_Mountain
	class Meta:
		get_latest_by = 'record'
		


class moWLR_Queen(Audit):
	mvWLR_Queen = models.BigIntegerField(verbose_name='WLR-Queen', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvWLR_Queen
	class Meta:
		get_latest_by = 'record'
		


class moWLR_Cabin(Audit):
	mvWLR_Cabin = models.BigIntegerField(verbose_name='WLR-Cabin', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvWLR_Cabin
	class Meta:
		get_latest_by = 'record'
		


class moWLR_Slipper(Audit):
	mvWLR_Slipper = models.BigIntegerField(verbose_name='WLR-Slipper', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvWLR_Slipper
	class Meta:
		get_latest_by = 'record'
		


class moWLR_Pole(Audit):
	mvWLR_Pole = models.BigIntegerField(verbose_name='WLR-Pole', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvWLR_Pole
	class Meta:
		get_latest_by = 'record'
		


class moWLR_Village(Audit):
	mvWLR_Village = models.BigIntegerField(verbose_name='WLR-Village', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvWLR_Village
	class Meta:
		get_latest_by = 'record'
		


class moWLR_String(Audit):
	mvWLR_String = models.BigIntegerField(verbose_name='WLR-String', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvWLR_String
	class Meta:
		get_latest_by = 'record'
		


class moWLR_Ticket(Audit):
	mvWLR_Ticket = models.BigIntegerField(verbose_name='WLR-Ticket', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvWLR_Ticket
	class Meta:
		get_latest_by = 'record'
		


class moWLR_Troops(Audit):
	mvWLR_Troops = models.BigIntegerField(verbose_name='WLR-Troops', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvWLR_Troops
	class Meta:
		get_latest_by = 'record'
		


class moWLR_Grass(Audit):
	mvWLR_Grass = models.BigIntegerField(verbose_name='WLR-Grass', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvWLR_Grass
	class Meta:
		get_latest_by = 'record'
		


class moWLR_Engine(Audit):
	mvWLR_Engine = models.BigIntegerField(verbose_name='WLR-Engine', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvWLR_Engine
	class Meta:
		get_latest_by = 'record'
		


class moWLR_Total_Yes(Audit):
	mvWLR_Total_Yes = models.BigIntegerField(verbose_name='WLR-TOTAL Yes', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvWLR_Total_Yes
	class Meta:
		get_latest_by = 'record'
		


class moWLR_Total_No(Audit):
	mvWLR_Total_No = models.BigIntegerField(verbose_name='WLR-TOTAL No', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvWLR_Total_No
	class Meta:
		get_latest_by = 'record'
		


class moWLrecall_Butter(Audit):
	mvWLrecall_Butter = models.BooleanField(verbose_name='WLRecall-Butter')
	def __unicode__(self):
		return "%s" % self.mvWLrecall_Butter
	class Meta:
		get_latest_by = 'record'
		


class moWLrecall_Arm(Audit):
	mvWLrecall_Arm = models.BooleanField(verbose_name='WLRecall-Arm')
	def __unicode__(self):
		return "%s" % self.mvWLrecall_Arm
	class Meta:
		get_latest_by = 'record'
		


class moWLrecall_Shore(Audit):
	mvWLrecall_Shore = models.BooleanField(verbose_name='WLRecall-Shore')
	def __unicode__(self):
		return "%s" % self.mvWLrecall_Shore
	class Meta:
		get_latest_by = 'record'
		


class moWLrecall_Letter(Audit):
	mvWLrecall_Letter = models.BooleanField(verbose_name='WLRecall-Letter')
	def __unicode__(self):
		return "%s" % self.mvWLrecall_Letter
	class Meta:
		get_latest_by = 'record'
		


class moWLRecall_Queen(Audit):
	mvWLRecall_Queen = models.BooleanField(verbose_name='WLRecall-Queen')
	def __unicode__(self):
		return "%s" % self.mvWLRecall_Queen
	class Meta:
		get_latest_by = 'record'
		


class moWLRecall_Cabin(Audit):
	mvWLRecall_Cabin = models.BooleanField(verbose_name='WLRecall-Cabin')
	def __unicode__(self):
		return "%s" % self.mvWLRecall_Cabin
	class Meta:
		get_latest_by = 'record'
		


class moWLRecall_Pole(Audit):
	mvWLRecall_Pole = models.BooleanField(verbose_name='WLRecall-Pole')
	def __unicode__(self):
		return "%s" % self.mvWLRecall_Pole
	class Meta:
		get_latest_by = 'record'
		


class moWLRecall_Ticket(Audit):
	mvWLRecall_Ticket = models.BooleanField(verbose_name='WLRecall-Ticket')
	def __unicode__(self):
		return "%s" % self.mvWLRecall_Ticket
	class Meta:
		get_latest_by = 'record'
		


class moWLRecall_Grass(Audit):
	mvWLRecall_Grass = models.BooleanField(verbose_name='WLRecall-Grass')
	def __unicode__(self):
		return "%s" % self.mvWLRecall_Grass
	class Meta:
		get_latest_by = 'record'
		


class moWLRecall_Engine(Audit):
	mvWLRecall_Engine = models.BooleanField(verbose_name='WLRecall-Engine')
	def __unicode__(self):
		return "%s" % self.mvWLRecall_Engine
	class Meta:
		get_latest_by = 'record'
		


class moWLR_Intrusions(Audit):
	mvWLR_Intrusions = models.CharField(verbose_name='WLR-Intrusions', blank=False, null=False, max_length=30)
	def __unicode__(self):
		return "%s" % self.mvWLR_Intrusions
	class Meta:
		get_latest_by = 'record'
		


class moWLRecall_Total_Correct(Audit):
	mvWLRecall_Total_Correct = models.BigIntegerField(verbose_name='WLRecall-Total Correct', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvWLRecall_Total_Correct
	class Meta:
		get_latest_by = 'record'
		


class moWLRecall_Total_Intrusions(Audit):
	mvWLRecall_Total_Intrusions = models.BigIntegerField(verbose_name='WLRecall-Total Intrusions', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvWLRecall_Total_Intrusions
	class Meta:
		get_latest_by = 'record'
		


class moIADL_Name(Audit):
	mvIADL_Name = models.CharField(verbose_name='IADL-Name of Patient', blank=False, null=False, max_length=30)
	def __unicode__(self):
		return "%s" % self.mvIADL_Name
	class Meta:
		get_latest_by = 'record'
		


class moIADL_Date(Audit):
	mvIADL_Date = models.DateField(verbose_name='IADL-Date', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvIADL_Date
	class Meta:
		get_latest_by = 'record'
		


class moIADL_Telephone(Audit):
	mvIADL_Telephone = models.RadioButton(verbose_name='IADL-Using Telephone', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvIADL_Telephone
	class Meta:
		get_latest_by = 'record'
		


class moIADL_Travelling(Audit):
	mvIADL_Travelling = models.RadioButton(verbose_name='IADL-Travelling', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvIADL_Travelling
	class Meta:
		get_latest_by = 'record'
		


class moIADL_Shopping(Audit):
	mvIADL_Shopping = models.RadioButton(verbose_name='IADL-Shopping', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvIADL_Shopping
	class Meta:
		get_latest_by = 'record'
		


class moIADL_PrepMeals(Audit):
	mvIADL_PrepMeals = models.RadioButton(verbose_name='IADL-Preparing Meals', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvIADL_PrepMeals
	class Meta:
		get_latest_by = 'record'
		


class moIADL_Housework(Audit):
	mvIADL_Housework = models.RadioButton(verbose_name='IADL-Housework', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvIADL_Housework
	class Meta:
		get_latest_by = 'record'
		


class moIADL_Medicine(Audit):
	mvIADL_Medicine = models.RadioButton(verbose_name='IADL_Taking Medicine', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvIADL_Medicine
	class Meta:
		get_latest_by = 'record'
		


class moIADL_ManagingMoney(Audit):
	mvIADL_ManagingMoney = models.RadioButton(verbose_name='IADL-Managing Money', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvIADL_ManagingMoney
	class Meta:
		get_latest_by = 'record'
		


class moGDS_Hospital(Audit):
	mvGDS_Hospital = models.RadioButton(verbose_name='GDS-Hospital Location', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvGDS_Hospital
	class Meta:
		get_latest_by = 'record'
		


class moGDS_SatisfiedLife(Audit):
	mvGDS_SatisfiedLife = models.RadioButton(verbose_name='GDS-1. Are you basically satisfied with your life', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvGDS_SatisfiedLife
	class Meta:
		get_latest_by = 'record'
		


class moGDS_ActivityInterests(Audit):
	mvGDS_ActivityInterests = models.RadioButton(verbose_name='GDS-2. Have you dropped many of your activities and interest', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvGDS_ActivityInterests
	class Meta:
		get_latest_by = 'record'
		


class moGDS_LifeEmpty(Audit):
	mvGDS_LifeEmpty = models.RadioButton(verbose_name='GDS-3. Do you feel your life is empty', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvGDS_LifeEmpty
	class Meta:
		get_latest_by = 'record'
		


class moGDS_Boredom(Audit):
	mvGDS_Boredom = models.RadioButton(verbose_name='GDS-4. Do you often get bored', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvGDS_Boredom
	class Meta:
		get_latest_by = 'record'
		


class moGDS_GoodSpirits(Audit):
	mvGDS_GoodSpirits = models.RadioButton(verbose_name='GDS-5. Are you in good spirits most of the time', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvGDS_GoodSpirits
	class Meta:
		get_latest_by = 'record'
		


class moGDS_Fear(Audit):
	mvGDS_Fear = models.RadioButton(verbose_name='GDS-6. Are you afraid that something bad is going to happen to you', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvGDS_Fear
	class Meta:
		get_latest_by = 'record'
		


class moGDS_Happiness(Audit):
	mvGDS_Happiness = models.RadioButton(verbose_name='GDS-7. Do you feel happy most of the time', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvGDS_Happiness
	class Meta:
		get_latest_by = 'record'
		


class moGDS_Helplessness(Audit):
	mvGDS_Helplessness = models.RadioButton(verbose_name='GDS-8. Do you often feel helpless', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvGDS_Helplessness
	class Meta:
		get_latest_by = 'record'
		


class moGDS_PreferStayHome(Audit):
	mvGDS_PreferStayHome = models.RadioButton(verbose_name='GDS-9. Do you prefer to stay home, rather than going out and doing new things', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvGDS_PreferStayHome
	class Meta:
		get_latest_by = 'record'
		


class moGDS_Memory(Audit):
	mvGDS_Memory = models.RadioButton(verbose_name='GDS-10. Do you feel you have more problems with memory than most', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvGDS_Memory
	class Meta:
		get_latest_by = 'record'
		


class moGDS_AttitiudeLiving(Audit):
	mvGDS_AttitiudeLiving = models.RadioButton(verbose_name='GDS-11. Do you think it\'s wonderful to be alive now', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvGDS_AttitiudeLiving
	class Meta:
		get_latest_by = 'record'
		


class moGDS_Worthlessness(Audit):
	mvGDS_Worthlessness = models.RadioButton(verbose_name='GDS-12. Do you feel pretty worthless the way you are now?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvGDS_Worthlessness
	class Meta:
		get_latest_by = 'record'
		


class moGDS_Energy(Audit):
	mvGDS_Energy = models.RadioButton(verbose_name='GDS-13. Do you feel full of energy?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvGDS_Energy
	class Meta:
		get_latest_by = 'record'
		


class moGDS_SituationHopeless(Audit):
	mvGDS_SituationHopeless = models.RadioButton(verbose_name='GDS-14. Do you feel that your situation is hopeless?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvGDS_SituationHopeless
	class Meta:
		get_latest_by = 'record'
		


class moGDS_BetterOff(Audit):
	mvGDS_BetterOff = models.RadioButton(verbose_name='GDS-15. Do you think that most people are better off than you are?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvGDS_BetterOff
	class Meta:
		get_latest_by = 'record'
		


class moGDS_Signature(Audit):
	mvGDS_Signature = models.CharField(verbose_name='GDS-Signature', blank=False, null=False, max_length=30)
	def __unicode__(self):
		return "%s" % self.mvGDS_Signature
	class Meta:
		get_latest_by = 'record'
		


class moGDS_Date(Audit):
	mvGDS_Date = models.CharField(verbose_name='GDS-Date', blank=False, null=False, max_length=30)
	def __unicode__(self):
		return "%s" % self.mvGDS_Date
	class Meta:
		get_latest_by = 'record'
		


class moGDS_Total(Audit):
	mvGDS_Total = models.BigIntegerField(verbose_name='GDS_TOTAL score', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvGDS_Total
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_PatientName(Audit):
	mvSAGE_PatientName = models.CharField(verbose_name='SAGE-Patient Name', blank=False, null=False, max_length=30)
	def __unicode__(self):
		return "%s" % self.mvSAGE_PatientName
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_Date(Audit):
	mvSAGE_Date = models.DateField(verbose_name='SAGE-Date Completed', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvSAGE_Date
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_CompletedBy(Audit):
	mvSAGE_CompletedBy = models.RadioButton(verbose_name='SAGE_Completed by', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvSAGE_CompletedBy
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_Other_Relationship(Audit):
	mvSAGE_Other_Relationship = models.CharField(verbose_name='SAGE-Other person-relationship to participant', blank=False, null=False, max_length=30)
	def __unicode__(self):
		return "%s" % self.mvSAGE_Other_Relationship
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_TelephoneAdministration(Audit):
	mvSAGE_TelephoneAdministration = models.RadioButton(verbose_name='SAGE_Is this being administered via telephone?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvSAGE_TelephoneAdministration
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_Lawton(Audit):
	mvSAGE_Lawton = models.RadioButton(verbose_name='SAGE_Lawton IADL also administered?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvSAGE_Lawton
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_SAGECompleted(Audit):
	mvSAGE_SAGECompleted = models.RadioButton(verbose_name='SAGE-If also administered, then SAGE done:', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvSAGE_SAGECompleted
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_Attention(Audit):
	mvSAGE_Attention = models.RadioButton(verbose_name='SAGE-1. Keeping your attention or :train of thought" during a conversation', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvSAGE_Attention
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_Remembering(Audit):
	mvSAGE_Remembering = models.RadioButton(verbose_name='SAGE-2. Remembering things that happened a few days before? (e.g. conversation, people visiting)', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvSAGE_Remembering
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_ConcentrationGameBook(Audit):
	mvSAGE_ConcentrationGameBook = models.RadioButton(verbose_name='SAGE-3. Playing a game or reading a book that requires concentration? (of games: crosswords, checkers, chess)', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvSAGE_ConcentrationGameBook
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_Multitask(Audit):
	mvSAGE_Multitask = models.RadioButton(verbose_name='SAGE-4. Ability to switch between things that are happening at the same time? (e.g. making tea and talking to someone)', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvSAGE_Multitask
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_FindWayBuilding(Audit):
	mvSAGE_FindWayBuilding = models.RadioButton(verbose_name='SAGE-5. Finding your way around a new building? (e.g. hospital/clinic)', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvSAGE_FindWayBuilding
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_OrganizeSocial(Audit):
	mvSAGE_OrganizeSocial = models.RadioButton(verbose_name='SAGE-6. Organizing a trip or social activities', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvSAGE_OrganizeSocial
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_FinanceShopping(Audit):
	mvSAGE_FinanceShopping = models.RadioButton(verbose_name='SAGE-7. Doing your own finances or shopping?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvSAGE_FinanceShopping
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_OrganizeMeds(Audit):
	mvSAGE_OrganizeMeds = models.RadioButton(verbose_name='SAGE-8. Organizing and taking your medications', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvSAGE_OrganizeMeds
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_MealsLaundry(Audit):
	mvSAGE_MealsLaundry = models.RadioButton(verbose_name='SAGE-9. Preparing a meal and/or doing laundry', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvSAGE_MealsLaundry
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_Driving(Audit):
	mvSAGE_Driving = models.RadioButton(verbose_name='SAGE-10 a) Driving', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvSAGE_Driving
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_PublicTrans(Audit):
	mvSAGE_PublicTrans = models.RadioButton(verbose_name='SAGE-Driving b) Using public transportation', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvSAGE_PublicTrans
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_Stairs(Audit):
	mvSAGE_Stairs = models.RadioButton(verbose_name='SAGE-11. Using stairs? (one flight)', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvSAGE_Stairs
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_Stairs_Yes(Audit):
	mvSAGE_Stairs_Yes = models.RadioButton(verbose_name='SAGE-Stairs-If yes', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvSAGE_Stairs_Yes
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_StairsModerate_Help(Audit):
	mvSAGE_StairsModerate_Help = models.RadioButton(verbose_name='SAGE-Stairs-If Moderate, do you require help?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvSAGE_StairsModerate_Help
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_WalkingDifficulty(Audit):
	mvSAGE_WalkingDifficulty = models.RadioButton(verbose_name='SAGE-12. Walking? (approx. 10m or 32ft or 14 steps)', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvSAGE_WalkingDifficulty
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_WalkingModerate_Help(Audit):
	mvSAGE_WalkingModerate_Help = models.RadioButton(verbose_name='SAGE-Walking-If moderate, do you require help?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvSAGE_WalkingModerate_Help
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_Walking_Yes(Audit):
	mvSAGE_Walking_Yes = models.RadioButton(verbose_name='SAGE-Walking-If yes', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvSAGE_Walking_Yes
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_Dressing(Audit):
	mvSAGE_Dressing = models.RadioButton(verbose_name='SAGE-13. Dressing?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvSAGE_Dressing
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_DressingModerate(Audit):
	mvSAGE_DressingModerate = models.RadioButton(verbose_name='SAGE-Dressing-If moderate, do you require help from another person?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvSAGE_DressingModerate
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_Transfer_BedToChair(Audit):
	mvSAGE_Transfer_BedToChair = models.RadioButton(verbose_name='SAGE-14. Transfer from bed to chair', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvSAGE_Transfer_BedToChair
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_TransferModerate_Help(Audit):
	mvSAGE_TransferModerate_Help = models.RadioButton(verbose_name='SAGE-Transfer from bed to chair-If moderate, do you require help from another person?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvSAGE_TransferModerate_Help
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_BathingToileting(Audit):
	mvSAGE_BathingToileting = models.RadioButton(verbose_name='SAGE-15. Bathing and Toileting', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvSAGE_BathingToileting
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_BathingToiletingModerate_Help(Audit):
	mvSAGE_BathingToiletingModerate_Help = models.RadioButton(verbose_name='SAGE-Bathing/Toileting-If moderate, do you require help from another person?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvSAGE_BathingToiletingModerate_Help
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_Score(Audit):
	mvSAGE_Score = models.BigIntegerField(verbose_name='SAGE_Score', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvSAGE_Score
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_ActivityPerf_MemoryProblems(Audit):
	mvSAGE_ActivityPerf_MemoryProblems = models.BooleanField(verbose_name='SAGE-16. Activity Performance-Memory problems')
	def __unicode__(self):
		return "%s" % self.mvSAGE_ActivityPerf_MemoryProblems
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_ActivityPerf_Arthritis(Audit):
	mvSAGE_ActivityPerf_Arthritis = models.BooleanField(verbose_name='SAGE-16. Activity Performance-Arthritis')
	def __unicode__(self):
		return "%s" % self.mvSAGE_ActivityPerf_Arthritis
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_ActivityPerf_ShortnessBreath(Audit):
	mvSAGE_ActivityPerf_ShortnessBreath = models.BooleanField(verbose_name='SAGE-16. Activity Performance-Shortness of breath')
	def __unicode__(self):
		return "%s" % self.mvSAGE_ActivityPerf_ShortnessBreath
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_ActivityPerf_ChestPain(Audit):
	mvSAGE_ActivityPerf_ChestPain = models.BooleanField(verbose_name='SAGE-16. Activity Performance-Chest Pain')
	def __unicode__(self):
		return "%s" % self.mvSAGE_ActivityPerf_ChestPain
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_ActivityPerf_PhysicalInjury(Audit):
	mvSAGE_ActivityPerf_PhysicalInjury = models.BooleanField(verbose_name='SAGE-16. Activity Performance-Physical Injury')
	def __unicode__(self):
		return "%s" % self.mvSAGE_ActivityPerf_PhysicalInjury
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_ActivityPerf_StrokeTIA(Audit):
	mvSAGE_ActivityPerf_StrokeTIA = models.BooleanField(verbose_name='SAGE-16. Activity Performance-Stroke or TIA')
	def __unicode__(self):
		return "%s" % self.mvSAGE_ActivityPerf_StrokeTIA
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_ActivityPerf_HeartFailure(Audit):
	mvSAGE_ActivityPerf_HeartFailure = models.BooleanField(verbose_name='SAGE-16. Activity Performance-Heart Failure')
	def __unicode__(self):
		return "%s" % self.mvSAGE_ActivityPerf_HeartFailure
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_ActivityPerf_VisionLoss(Audit):
	mvSAGE_ActivityPerf_VisionLoss = models.RadioButton(verbose_name='SAGE-16. Activity Performance-Loss of Vision', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvSAGE_ActivityPerf_VisionLoss
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_ActivityPerf_Unsteadiness(Audit):
	mvSAGE_ActivityPerf_Unsteadiness = models.BooleanField(verbose_name='SAGE-16. Activity Performance-Unsteadiness')
	def __unicode__(self):
		return "%s" % self.mvSAGE_ActivityPerf_Unsteadiness
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_ActivityPerf_Other(Audit):
	mvSAGE_ActivityPerf_Other = models.CharField(verbose_name='SAGE-16. Activity Performance-Other', blank=False, null=False, max_length=30)
	def __unicode__(self):
		return "%s" % self.mvSAGE_ActivityPerf_Other
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_ActivityPerf_None(Audit):
	mvSAGE_ActivityPerf_None = models.BooleanField(verbose_name='SAGE-16. Activity Performance-None of the Abover')
	def __unicode__(self):
		return "%s" % self.mvSAGE_ActivityPerf_None
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_ActivityPerf_NotSure(Audit):
	mvSAGE_ActivityPerf_NotSure = models.BooleanField(verbose_name='SAGE-16. Activity Performance-Not sure')
	def __unicode__(self):
		return "%s" % self.mvSAGE_ActivityPerf_NotSure
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_InvestigatorNurse_Signature(Audit):
	mvSAGE_InvestigatorNurse_Signature = models.CharField(verbose_name='SAGE_Site Investigator/Nurse Signature', blank=False, null=False, max_length=30)
	def __unicode__(self):
		return "%s" % self.mvSAGE_InvestigatorNurse_Signature
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_InvestigatorNurse_PrintName(Audit):
	mvSAGE_InvestigatorNurse_PrintName = models.CharField(verbose_name='SAGE-Site Investigator/Nurse Printed Name', blank=False, null=False, max_length=30)
	def __unicode__(self):
		return "%s" % self.mvSAGE_InvestigatorNurse_PrintName
	class Meta:
		get_latest_by = 'record'
		


class moSAGE_EndDate(Audit):
	mvSAGE_EndDate = models.DateField(verbose_name='SAGE-End Date', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvSAGE_EndDate
	class Meta:
		get_latest_by = 'record'
		


class moCBS_CaregiverName(Audit):
	mvCBS_CaregiverName = models.CharField(verbose_name='CBS_Caregiver Name', blank=False, null=False, max_length=30)
	def __unicode__(self):
		return "%s" % self.mvCBS_CaregiverName
	class Meta:
		get_latest_by = 'record'
		


class moCBS_Date(Audit):
	mvCBS_Date = models.DateField(verbose_name='CBS-Date', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCBS_Date
	class Meta:
		get_latest_by = 'record'
		


class moCBS_AsksMoreThanNeeds(Audit):
	mvCBS_AsksMoreThanNeeds = models.RadioButton(verbose_name='CBS-1. Do you feel that your relative asks for more help than he or she needs?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCBS_AsksMoreThanNeeds
	class Meta:
		get_latest_by = 'record'
		


class moCBS_NotEnoughTimeForSelf(Audit):
	mvCBS_NotEnoughTimeForSelf = models.RadioButton(verbose_name='CBS-2. Do you feel that because of the time you spend with your relative, you do not have enough time for yourself?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCBS_NotEnoughTimeForSelf
	class Meta:
		get_latest_by = 'record'
		


class moCBS_Stress_Overwhelmed(Audit):
	mvCBS_Stress_Overwhelmed = models.RadioButton(verbose_name='CBS-3. Do you feel stressed between caring for your relative and trying to meet other responsibilities', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCBS_Stress_Overwhelmed
	class Meta:
		get_latest_by = 'record'
		


class moCBS_Embarassment(Audit):
	mvCBS_Embarassment = models.RadioButton(verbose_name='CBS-4. Do you feel embarrassed over your relatives behavior?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCBS_Embarassment
	class Meta:
		get_latest_by = 'record'
		


class moCBS_Anger(Audit):
	mvCBS_Anger = models.RadioButton(verbose_name='CBS-5. Do you feel angry when you are around your relative?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCBS_Anger
	class Meta:
		get_latest_by = 'record'
		


class moCBS_Relative_NegativeEffectRelationship(Audit):
	mvCBS_Relative_NegativeEffectRelationship = models.RadioButton(verbose_name='CBS-6. Do you feel that your relative currently affects your relationship with other family members or friends in a negative way?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCBS_Relative_NegativeEffectRelationship
	class Meta:
		get_latest_by = 'record'
		


class moCBS_FearFutureRelative(Audit):
	mvCBS_FearFutureRelative = models.RadioButton(verbose_name='CBS-7. Are you afraid about what the future holds for your relative?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCBS_FearFutureRelative
	class Meta:
		get_latest_by = 'record'
		


class moCBS_RelativeDependent(Audit):
	mvCBS_RelativeDependent = models.RadioButton(verbose_name='CBS-8. Do you feel your relative is dependent on you?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCBS_RelativeDependent
	class Meta:
		get_latest_by = 'record'
		


class moCBS_Strained(Audit):
	mvCBS_Strained = models.RadioButton(verbose_name='CBS-9. Do you feel strained when you are around your relative?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCBS_Strained
	class Meta:
		get_latest_by = 'record'
		


class moCBS_HealthSuffered(Audit):
	mvCBS_HealthSuffered = models.RadioButton(verbose_name='CBS-10. Do you feel your health has suffered because of your involvement with your relative?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCBS_HealthSuffered
	class Meta:
		get_latest_by = 'record'
		


class moCBS_LackOfPrivacy(Audit):
	mvCBS_LackOfPrivacy = models.RadioButton(verbose_name='CBS-11. Do you feel that you do not have as much privacy as you would like, because of your relative?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCBS_LackOfPrivacy
	class Meta:
		get_latest_by = 'record'
		


class moCBS_SocialLifeSuffer(Audit):
	mvCBS_SocialLifeSuffer = models.RadioButton(verbose_name='CBS-12. Do you feel that your social life has suffered because you are caring for your relative?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCBS_SocialLifeSuffer
	class Meta:
		get_latest_by = 'record'
		


class moCBS_UncomfortableSocialSetting(Audit):
	mvCBS_UncomfortableSocialSetting = models.RadioButton(verbose_name='CBS-13. Do you feel uncomfortable about having friends over, because of your relative?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCBS_UncomfortableSocialSetting
	class Meta:
		get_latest_by = 'record'
		


class moCBS_RelativeDependentExclusively(Audit):
	mvCBS_RelativeDependentExclusively = models.RadioButton(verbose_name='CBS-14. Do you feel that your relative seems to expect you to take care of him or her, as if you were the only one he or she could depend on?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCBS_RelativeDependentExclusively
	class Meta:
		get_latest_by = 'record'
		


class moCBS_MoneyExpenses(Audit):
	mvCBS_MoneyExpenses = models.RadioButton(verbose_name='CBS-15. Do you feel that you do not have enough money to care for your relative, in addition to the rest of your expenses?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCBS_MoneyExpenses
	class Meta:
		get_latest_by = 'record'
		


class moCBS_UnableToCareMuchLonger(Audit):
	mvCBS_UnableToCareMuchLonger = models.RadioButton(verbose_name='CBS-16. Do you feel that you will be unable to take care of your relative much longer?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCBS_UnableToCareMuchLonger
	class Meta:
		get_latest_by = 'record'
		


class moCBS_LossControlLife(Audit):
	mvCBS_LossControlLife = models.RadioButton(verbose_name='CBS-17. Do you feel you have lost control of your life since your relative\'s illness?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCBS_LossControlLife
	class Meta:
		get_latest_by = 'record'
		


class moCBS_LeaveCareSomeoneElse(Audit):
	mvCBS_LeaveCareSomeoneElse = models.RadioButton(verbose_name='CBS-18. Do you wish you could just leave the care of your relative to someone else?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCBS_LeaveCareSomeoneElse
	class Meta:
		get_latest_by = 'record'
		


class moCBS_Uncertainty(Audit):
	mvCBS_Uncertainty = models.RadioButton(verbose_name='CBS-19. Do you feel uncertain about what to do about your relative?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCBS_Uncertainty
	class Meta:
		get_latest_by = 'record'
		


class moCBS_FeelsShouldDoMore(Audit):
	mvCBS_FeelsShouldDoMore = models.RadioButton(verbose_name='CBS-20. Do you feel you should be doing more for your relative?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCBS_FeelsShouldDoMore
	class Meta:
		get_latest_by = 'record'
		


class moCBS_BetterJob(Audit):
	mvCBS_BetterJob = models.RadioButton(verbose_name='CBS-21. Do you feel you could do a better job in caring for your relative?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCBS_BetterJob
	class Meta:
		get_latest_by = 'record'
		


class moCBS_Burdened(Audit):
	mvCBS_Burdened = models.RadioButton(verbose_name='CBS-22. Overall, how burdened do you feel in caring for your r', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCBS_Burdened
	class Meta:
		get_latest_by = 'record'
		


class moCBS_Total_Score(Audit):
	mvCBS_Total_Score = models.BigIntegerField(verbose_name='CBS-Total Score', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvCBS_Total_Score
	class Meta:
		get_latest_by = 'record'
		


class moFBI_CaregiverName(Audit):
	mvFBI_CaregiverName = models.CharField(verbose_name='FBI-Caregiver Name', blank=False, null=False, max_length=30)
	def __unicode__(self):
		return "%s" % self.mvFBI_CaregiverName
	class Meta:
		get_latest_by = 'record'
		


class moFBI_Relationship(Audit):
	mvFBI_Relationship = models.CharField(verbose_name='FBI-Relationship', blank=False, null=False, max_length=30)
	def __unicode__(self):
		return "%s" % self.mvFBI_Relationship
	class Meta:
		get_latest_by = 'record'
		


class moFBI_Date(Audit):
	mvFBI_Date = models.DateField(verbose_name='FBI_Date', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvFBI_Date
	class Meta:
		get_latest_by = 'record'
		


class moFBI_Apathy(Audit):
	mvFBI_Apathy = models.RadioButton(verbose_name='FBI-1. Apathy: Has s/he lost interest in friends or daily activities', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvFBI_Apathy
	class Meta:
		get_latest_by = 'record'
		


class moFBI_Aspontaneity(Audit):
	mvFBI_Aspontaneity = models.RadioButton(verbose_name='FBI-2. Apontaneity: Does s/he start things on his/her own, or does s/he have to be asked?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvFBI_Aspontaneity
	class Meta:
		get_latest_by = 'record'
		


class moFBI_Indifference_EmotionalFlatness(Audit):
	mvFBI_Indifference_EmotionalFlatness = models.RadioButton(verbose_name='FBI-3. Indifference, Emotional Flatness: Does s/he respond to occasions of joy or sadness as much as ever, or has s/he lost emotional responsiveness?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvFBI_Indifference_EmotionalFlatness
	class Meta:
		get_latest_by = 'record'
		


class moFBI_Inflexibility(Audit):
	mvFBI_Inflexibility = models.RadioButton(verbose_name='FBI-4. Inflexibility: Can s/he change his/her mind with reason or does s/he appear stubbor or rigid in thinking lately?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvFBI_Inflexibility
	class Meta:
		get_latest_by = 'record'
		


class moFBI_Concreteness(Audit):
	mvFBI_Concreteness = models.RadioButton(verbose_name='FBI-5. Concreteness: Does s/he interpret what is being said appropriately or does s/he choose only the concrete meanings of what is being said?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvFBI_Concreteness
	class Meta:
		get_latest_by = 'record'
		


class moFBI_PersonalNeglect(Audit):
	mvFBI_PersonalNeglect = models.RadioButton(verbose_name='FBI-6. Personal Neglect: Does s/he take as much care of his/her personal hygiene and appearance as usual?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvFBI_PersonalNeglect
	class Meta:
		get_latest_by = 'record'
		


class moFBI_Disorganization(Audit):
	mvFBI_Disorganization = models.RadioButton(verbose_name='FBI-7. Disorganization: Can s/he plan and organize complex activity or is s/he easily distractible, impersistent, or unable to complete a job?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvFBI_Disorganization
	class Meta:
		get_latest_by = 'record'
		


class moFBI_Inattention(Audit):
	mvFBI_Inattention = models.RadioButton(verbose_name='FBI-8. Inattention: Odes s/he pay attention to what is going on or does s/he seem to loose track or not follow at all?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvFBI_Inattention
	class Meta:
		get_latest_by = 'record'
		


class moFBI_LossOfInsight(Audit):
	mvFBI_LossOfInsight = models.RadioButton(verbose_name='FBI-9. Loss of Insight: Is s/he aware of any problems or changes, or does s/he seem unaware of them ro deny them when discussed?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvFBI_LossOfInsight
	class Meta:
		get_latest_by = 'record'
		


class moFBI_Logopenia(Audit):
	mvFBI_Logopenia = models.RadioButton(verbose_name='FBI-10. Logopenia: Has s/he been talking clearly or has s/he been making errors in speech? Is there slurring or hesitation?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvFBI_Logopenia
	class Meta:
		get_latest_by = 'record'
		


class moFBI_VerbalApraxia(Audit):
	mvFBI_VerbalApraxia = models.RadioButton(verbose_name='FBI-11. Verbal Apraxia: Has s/he been talking clearly or has s/he been making errors in speech? Is there slurring or hesitation?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvFBI_VerbalApraxia
	class Meta:
		get_latest_by = 'record'
		


class moFBI_Perseveration(Audit):
	mvFBI_Perseveration = models.RadioButton(verbose_name='FBI-12. Perseveration: Does s/he repeat or persevate actions or remarks?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvFBI_Perseveration
	class Meta:
		get_latest_by = 'record'
		


class moFBI_Irritibility(Audit):
	mvFBI_Irritibility = models.RadioButton(verbose_name='FBI-13. Irritibility: Has s/he been irritable, short-tempered, or is s/he reacting to stress or frustration as s/he always had', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvFBI_Irritibility
	class Meta:
		get_latest_by = 'record'
		


class moFBI_ExcessJocularity(Audit):
	mvFBI_ExcessJocularity = models.RadioButton(verbose_name='FBI-14. Excessive Jocularity: Has s/he been making jokes excessivly or offensively or at the wrong time', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvFBI_ExcessJocularity
	class Meta:
		get_latest_by = 'record'
		


class moFBI_PoorJudgement(Audit):
	mvFBI_PoorJudgement = models.RadioButton(verbose_name='FBI-15. Poor Judgement: Has s/he been using good judgement in decisions or in driving, or has s/he acted irresponsibly, neglectfully or in poor judgment?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvFBI_PoorJudgement
	class Meta:
		get_latest_by = 'record'
		


class moFBI_Impulsive(Audit):
	mvFBI_Impulsive = models.RadioButton(verbose_name='FBI-17. Impulsivity: Has s/he acted or spoken without thinking about consequences, or on the spur of the moment?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvFBI_Impulsive
	class Meta:
		get_latest_by = 'record'
		


class moFBI_Restlessness(Audit):
	mvFBI_Restlessness = models.RadioButton(verbose_name='FBI-18. Restlessness: Has s/he shown aggression, or shouted at anyone or hurt them physically?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvFBI_Restlessness
	class Meta:
		get_latest_by = 'record'
		


class moFBI_Agression(Audit):
	mvFBI_Agression = models.RadioButton(verbose_name='FBI-19. Aggression: Has s/he shown aggression, or shouted at anyone or hurt them physically?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvFBI_Agression
	class Meta:
		get_latest_by = 'record'
		


class moFBI_Hyperporality(Audit):
	mvFBI_Hyperporality = models.RadioButton(verbose_name='FBI-Hyperporality: Has s/he been drinking more than usual, eating excessively anything in sight, or even putting objects in his/her mouth?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvFBI_Hyperporality
	class Meta:
		get_latest_by = 'record'
		


class moFBI_Hypersexuality(Audit):
	mvFBI_Hypersexuality = models.RadioButton(verbose_name='FBI-Hypersexuality', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvFBI_Hypersexuality
	class Meta:
		get_latest_by = 'record'
		


class moFBI_UtilizationBehaviour(Audit):
	mvFBI_UtilizationBehaviour = models.RadioButton(verbose_name='FBI-22. Utilization Behaviour: Does s/he seem to need to touch, feel, examine, or pick up objects within reach and sight', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvFBI_UtilizationBehaviour
	class Meta:
		get_latest_by = 'record'
		


class moFBI_Incontinence(Audit):
	mvFBI_Incontinence = models.RadioButton(verbose_name='FBI-23. Incontinence: Does s/he have any problem using a hanf, and does it interfere with the other hand?', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvFBI_Incontinence
	class Meta:
		get_latest_by = 'record'
		


class moFBI_AlienHand(Audit):
	mvFBI_AlienHand = models.RadioButton(verbose_name='FBI-24. Alien Hand-Does s/he have any problem using a hand, and does it interfere with the other hand? (excluding arthritis, trauma, paralysis etc.)', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvFBI_AlienHand
	class Meta:
		get_latest_by = 'record'
		


class moFBI_TotalScore(Audit):
	mvFBI_TotalScore = models.RadioButton(verbose_name='FBI-Total Score', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvFBI_TotalScore
	class Meta:
		get_latest_by = 'record'
		


class moFAB_PatientClient_Name(Audit):
	mvFAB_PatientClient_Name = models.CharField(verbose_name='FAB-Patient/Client Name', blank=False, null=False, max_length=30)
	def __unicode__(self):
		return "%s" % self.mvFAB_PatientClient_Name
	class Meta:
		get_latest_by = 'record'
		


class moFAB_Age(Audit):
	mvFAB_Age = models.BigIntegerField(verbose_name='FAB-Age', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvFAB_Age
	class Meta:
		get_latest_by = 'record'
		


class moFAB_Date(Audit):
	mvFAB_Date = models.DateField(verbose_name='FAB-Date', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvFAB_Date
	class Meta:
		get_latest_by = 'record'
		


class moFAB_ChartFile_Number(Audit):
	mvFAB_ChartFile_Number = models.BigIntegerField(verbose_name='FAB-Chart/File Number', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvFAB_ChartFile_Number
	class Meta:
		get_latest_by = 'record'
		


class moFAB_AssessedBy(Audit):
	mvFAB_AssessedBy = models.CharField(verbose_name='FAB-Assessed By', blank=False, null=False, max_length=30)
	def __unicode__(self):
		return "%s" % self.mvFAB_AssessedBy
	class Meta:
		get_latest_by = 'record'
		


class moFAB_Sim_BananaOrange(Audit):
	mvFAB_Sim_BananaOrange = models.BigIntegerField(verbose_name='FAB-SIMILARITIES-1. A banana and orange', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvFAB_Sim_BananaOrange
	class Meta:
		get_latest_by = 'record'
		


class moFAB_Sim_TableChair(Audit):
	mvFAB_Sim_TableChair = models.BigIntegerField(verbose_name='FAB-SIMILARITIES-2. A table and a chair', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvFAB_Sim_TableChair
	class Meta:
		get_latest_by = 'record'
		


class moFAB_Sim_TulipRoseDaisy(Audit):
	mvFAB_Sim_TulipRoseDaisy = models.BigIntegerField(verbose_name='FAB-SIMILARITIES-3. A tulip, a rose and a daisy', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvFAB_Sim_TulipRoseDaisy
	class Meta:
		get_latest_by = 'record'
		


class moFAB_LexicalFluency(Audit):
	mvFAB_LexicalFluency = models.BigIntegerField(verbose_name='FAB-LEXICAL FLUENCY-Say as many words as you can beginning with the letter "S", except surnames or proper names', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvFAB_LexicalFluency
	class Meta:
		get_latest_by = 'record'
		


class moFAB_MotorSeriesProgramming(Audit):
	mvFAB_MotorSeriesProgramming = models.BigIntegerField(verbose_name='FAB-MOTOR SERIES PROGRAMMING', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvFAB_MotorSeriesProgramming
	class Meta:
		get_latest_by = 'record'
		


class moFAB_ConflictInstruct_111222(Audit):
	mvFAB_ConflictInstruct_111222 = models.BigIntegerField(verbose_name='FAB-CONFLICTING INSTRUCTIONS-Tap twice when I tap once: series 1-1-1 Tap once when I tap twice: 2-2-2', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvFAB_ConflictInstruct_111222
	class Meta:
		get_latest_by = 'record'
		


class moFAB_InhibControl_111222(Audit):
	mvFAB_InhibControl_111222 = models.BigIntegerField(verbose_name='FAB-GO NO GO (INHIBITORY CONTROL)-Tap once when I tap once: 1-1-1 Tap twice when I tap twice: 2-2-2', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvFAB_InhibControl_111222
	class Meta:
		get_latest_by = 'record'
		


class moFAB_EnviroControl(Audit):
	mvFAB_EnviroControl = models.BigIntegerField(verbose_name='FAB-ENVIRONMENTAL CONTROL', blank=False, null=False)
	def __unicode__(self):
		return "%s" % self.mvFAB_EnviroControl
	class Meta:
		get_latest_by = 'record'
		


class moFAB_TotalScore(Audit):
	mvFAB_TotalScore = models.BigIntegerField(verbose_name='FAB-Total Score', blank=False, null=True)
	def __unicode__(self):
		return "%s" % self.mvFAB_TotalScore
	class Meta:
		get_latest_by = 'record'
		


class moFAB_Comments(Audit):
	mvFAB_Comments = models.CharField(verbose_name='FAB-Comments', blank=True, null=False, max_length=100)
	def __unicode__(self):
		return "%s" % self.mvFAB_Comments
	class Meta:
		get_latest_by = 'record'
		


class moNIQPtName(Audit):
	mvNIQPtName = models.CharField(verbose_name='Nameofpatient', blank=True, null=True, max_length=50)
	def __unicode__(self):
		return "%s" % self.mvNIQPtName
	class Meta:
		get_latest_by = 'record'
		


class moNIQDate(Audit):
	mvNIQDate = models.DateField(verbose_name='Date', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvNIQDate
	class Meta:
		get_latest_by = 'record'
		


class moNIQInformant(Audit):
	mvNIQInformant = models.RadioButton(verbose_name='Informant', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvNIQInformant
	class Meta:
		get_latest_by = 'record'
		


class moNIQInformantOtherTxt(Audit):
	mvNIQInformantOtherTxt = models.RadioButton(verbose_name='Other', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvNIQInformantOtherTxt
	class Meta:
		get_latest_by = 'record'
		


class moNIQDelusions(Audit):
	mvNIQDelusions = models.RadioButton(verbose_name='Delusions', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvNIQDelusions
	class Meta:
		get_latest_by = 'record'
		


class moNIQDelSeverity(Audit):
	mvNIQDelSeverity = models.RadioButton(verbose_name='Severity', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvNIQDelSeverity
	class Meta:
		get_latest_by = 'record'
		


class moNIQDelDistress(Audit):
	mvNIQDelDistress = models.RadioButton(verbose_name='Distress', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvNIQDelDistress
	class Meta:
		get_latest_by = 'record'
		


class moNIQHallucinations(Audit):
	mvNIQHallucinations = models.RadioButton(verbose_name='Hallucinations', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvNIQHallucinations
	class Meta:
		get_latest_by = 'record'
		


class moNIQHallSeverity(Audit):
	mvNIQHallSeverity = models.RadioButton(verbose_name='Severity', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvNIQHallSeverity
	class Meta:
		get_latest_by = 'record'
		


class moNIQHallDistress(Audit):
	mvNIQHallDistress = models.RadioButton(verbose_name='Distress', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvNIQHallDistress
	class Meta:
		get_latest_by = 'record'
		


class moNIQAggitationAggression(Audit):
	mvNIQAggitationAggression = models.RadioButton(verbose_name='AggitationandAggression', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvNIQAggitationAggression
	class Meta:
		get_latest_by = 'record'
		


class moNIQAggSeverity(Audit):
	mvNIQAggSeverity = models.RadioButton(verbose_name='Severity', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvNIQAggSeverity
	class Meta:
		get_latest_by = 'record'
		


class moNIQAggDistress(Audit):
	mvNIQAggDistress = models.RadioButton(verbose_name='Distress', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvNIQAggDistress
	class Meta:
		get_latest_by = 'record'
		


class moNIQDepressionDysphoria(Audit):
	mvNIQDepressionDysphoria = models.RadioButton(verbose_name='DepressionandDysphoria', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvNIQDepressionDysphoria
	class Meta:
		get_latest_by = 'record'
		


class moNIQDepDysSeverity(Audit):
	mvNIQDepDysSeverity = models.RadioButton(verbose_name='Severity', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvNIQDepDysSeverity
	class Meta:
		get_latest_by = 'record'
		


class moNIQDepDysDistress(Audit):
	mvNIQDepDysDistress = models.RadioButton(verbose_name='Distress', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvNIQDepDysDistress
	class Meta:
		get_latest_by = 'record'
		


class moNIQAnxiety(Audit):
	mvNIQAnxiety = models.RadioButton(verbose_name='Anxiety', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvNIQAnxiety
	class Meta:
		get_latest_by = 'record'
		


class moNIQAnxSeverity(Audit):
	mvNIQAnxSeverity = models.RadioButton(verbose_name='Severity', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvNIQAnxSeverity
	class Meta:
		get_latest_by = 'record'
		


class moNIQAnxDistress(Audit):
	mvNIQAnxDistress = models.RadioButton(verbose_name='Distress', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvNIQAnxDistress
	class Meta:
		get_latest_by = 'record'
		


class moNIQElationEuphoria(Audit):
	mvNIQElationEuphoria = models.RadioButton(verbose_name='ElationandEuphoria', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvNIQElationEuphoria
	class Meta:
		get_latest_by = 'record'
		


class moNIQElaEupSeverity(Audit):
	mvNIQElaEupSeverity = models.RadioButton(verbose_name='Severity', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvNIQElaEupSeverity
	class Meta:
		get_latest_by = 'record'
		


class moNIQElaEupDistress(Audit):
	mvNIQElaEupDistress = models.RadioButton(verbose_name='Distress', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvNIQElaEupDistress
	class Meta:
		get_latest_by = 'record'
		


class moNIQApathyIndifference(Audit):
	mvNIQApathyIndifference = models.RadioButton(verbose_name='ApathyandIndifference', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvNIQApathyIndifference
	class Meta:
		get_latest_by = 'record'
		


class moNIQApaIndSeverity(Audit):
	mvNIQApaIndSeverity = models.RadioButton(verbose_name='Severity', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvNIQApaIndSeverity
	class Meta:
		get_latest_by = 'record'
		


class moNIQApaIndDistress(Audit):
	mvNIQApaIndDistress = models.RadioButton(verbose_name='Distress', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvNIQApaIndDistress
	class Meta:
		get_latest_by = 'record'
		


class moNIQDisinhibition(Audit):
	mvNIQDisinhibition = models.RadioButton(verbose_name='Disinhibition', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvNIQDisinhibition
	class Meta:
		get_latest_by = 'record'
		


class moNIQDisSeverity(Audit):
	mvNIQDisSeverity = models.RadioButton(verbose_name='Severity', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvNIQDisSeverity
	class Meta:
		get_latest_by = 'record'
		


class moNIQDisDistress(Audit):
	mvNIQDisDistress = models.RadioButton(verbose_name='Distress', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvNIQDisDistress
	class Meta:
		get_latest_by = 'record'
		


class moNIQIrritabilityLability(Audit):
	mvNIQIrritabilityLability = models.RadioButton(verbose_name='IrritabilityandLability', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvNIQIrritabilityLability
	class Meta:
		get_latest_by = 'record'
		


class moNIQIrrLabSeverity(Audit):
	mvNIQIrrLabSeverity = models.RadioButton(verbose_name='Severity', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvNIQIrrLabSeverity
	class Meta:
		get_latest_by = 'record'
		


class moNIQIffLabDistress(Audit):
	mvNIQIffLabDistress = models.RadioButton(verbose_name='Distress', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvNIQIffLabDistress
	class Meta:
		get_latest_by = 'record'
		


class moNIQMotorDisturbance(Audit):
	mvNIQMotorDisturbance = models.RadioButton(verbose_name='MotorDisturbance', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvNIQMotorDisturbance
	class Meta:
		get_latest_by = 'record'
		


class moNIQMotSeverity(Audit):
	mvNIQMotSeverity = models.RadioButton(verbose_name='Severity', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvNIQMotSeverity
	class Meta:
		get_latest_by = 'record'
		


class moNIQMotDistress(Audit):
	mvNIQMotDistress = models.RadioButton(verbose_name='Distress', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvNIQMotDistress
	class Meta:
		get_latest_by = 'record'
		


class moNIQNightTimeBehaviours(Audit):
	mvNIQNightTimeBehaviours = models.RadioButton(verbose_name='NighttimeBehaviours', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvNIQNightTimeBehaviours
	class Meta:
		get_latest_by = 'record'
		


class moNIQNigBehSeverity(Audit):
	mvNIQNigBehSeverity = models.RadioButton(verbose_name='Severity', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvNIQNigBehSeverity
	class Meta:
		get_latest_by = 'record'
		


class moNIQNigBehDistress(Audit):
	mvNIQNigBehDistress = models.RadioButton(verbose_name='Distress', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvNIQNigBehDistress
	class Meta:
		get_latest_by = 'record'
		


class moNIQAppetiteEating(Audit):
	mvNIQAppetiteEating = models.RadioButton(verbose_name='AppetiteandEating', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvNIQAppetiteEating
	class Meta:
		get_latest_by = 'record'
		


class moNIQAppEatSeverity(Audit):
	mvNIQAppEatSeverity = models.RadioButton(verbose_name='Severity', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvNIQAppEatSeverity
	class Meta:
		get_latest_by = 'record'
		


class moNIQAppEatDistress(Audit):
	mvNIQAppEatDistress = models.RadioButton(verbose_name='Distress', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvNIQAppEatDistress
	class Meta:
		get_latest_by = 'record'
		


class moRUDASPtName(Audit):
	mvRUDASPtName = models.CharField(verbose_name='Patient Name', blank=True, null=True, max_length=50)
	def __unicode__(self):
		return "%s" % self.mvRUDASPtName
	class Meta:
		get_latest_by = 'record'
		


class moRUDASDate(Audit):
	mvRUDASDate = models.DateField(verbose_name='Date', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvRUDASDate
	class Meta:
		get_latest_by = 'record'
		


class moRUDASVSORightFoot(Audit):
	mvRUDASVSORightFoot = models.BooleanField(verbose_name='Show me your right foot')
	def __unicode__(self):
		return "%s" % self.mvRUDASVSORightFoot
	class Meta:
		get_latest_by = 'record'
		


class moRUDASVSOLeftHand(Audit):
	mvRUDASVSOLeftHand = models.BooleanField(verbose_name='Show me your left hand')
	def __unicode__(self):
		return "%s" % self.mvRUDASVSOLeftHand
	class Meta:
		get_latest_by = 'record'
		


class moRUDASVSORtHndLftShoul(Audit):
	mvRUDASVSORtHndLftShoul = models.BooleanField(verbose_name='With your right hand touch your left shoulder')
	def __unicode__(self):
		return "%s" % self.mvRUDASVSORtHndLftShoul
	class Meta:
		get_latest_by = 'record'
		


class moRUDASVSOLftHndRtEar(Audit):
	mvRUDASVSOLftHndRtEar = models.BooleanField(verbose_name='With your left hand touch your right ear')
	def __unicode__(self):
		return "%s" % self.mvRUDASVSOLftHndRtEar
	class Meta:
		get_latest_by = 'record'
		


class moRUDASVSOObsLftKnee(Audit):
	mvRUDASVSOObsLftKnee = models.BooleanField(verbose_name='Which is (indicate/point to) my left knee')
	def __unicode__(self):
		return "%s" % self.mvRUDASVSOObsLftKnee
	class Meta:
		get_latest_by = 'record'
		


class moRUDASVSOObsRtElbow(Audit):
	mvRUDASVSOObsRtElbow = models.BooleanField(verbose_name='Which is (indicate/point to) my right elbow')
	def __unicode__(self):
		return "%s" % self.mvRUDASVSOObsRtElbow
	class Meta:
		get_latest_by = 'record'
		


class moRUDASVSORtHandObsLftEye(Audit):
	mvRUDASVSORtHandObsLftEye = models.BooleanField(verbose_name='With your right hand indicate/point to my left eye')
	def __unicode__(self):
		return "%s" % self.mvRUDASVSORtHandObsLftEye
	class Meta:
		get_latest_by = 'record'
		


class moRUDASVSOLftHandObsLftFoot(Audit):
	mvRUDASVSOLftHandObsLftFoot = models.BooleanField(verbose_name='With your left hand indicate/point to my left foot')
	def __unicode__(self):
		return "%s" % self.mvRUDASVSOLftHandObsLftFoot
	class Meta:
		get_latest_by = 'record'
		


class moRUDASVSOLTotalScore(Audit):
	mvRUDASVSOLTotalScore = models.BigIntegerField(verbose_name='Visuospatial Orientation Total Score', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvRUDASVSOLTotalScore
	class Meta:
		get_latest_by = 'record'
		


class moRUDASPRAXTotalScore(Audit):
	mvRUDASPRAXTotalScore = models.RadioButton(verbose_name='I am going to show you an action/exercise with my hands.  I want you to watch me and copy what I do.  Copy me when I do this... (One hand in fist, the other palm donw on table - alternate simultaneously.) Now do it with me:  Now I would like you to keep doing this action at this pace until I tell you to stop - approximately 10 seconds. (Demonstrate at moderate walking pace).', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvRUDASPRAXTotalScore
	class Meta:
		get_latest_by = 'record'
		


class moRUDASVCONDSquareImg(Audit):
	mvRUDASVCONDSquareImg = models.BooleanField(verbose_name='Has the person drawn a picture based on a square?')
	def __unicode__(self):
		return "%s" % self.mvRUDASVCONDSquareImg
	class Meta:
		get_latest_by = 'record'
		


class moRUDASVCONDInternalLines(Audit):
	mvRUDASVCONDInternalLines = models.BooleanField(verbose_name='Do all internal lines appear in person\'s drawing?')
	def __unicode__(self):
		return "%s" % self.mvRUDASVCONDInternalLines
	class Meta:
		get_latest_by = 'record'
		


class moRUDASVCONDExternalLines(Audit):
	mvRUDASVCONDExternalLines = models.BooleanField(verbose_name='Do all external lines appear in person\'s drawing?')
	def __unicode__(self):
		return "%s" % self.mvRUDASVCONDExternalLines
	class Meta:
		get_latest_by = 'record'
		


class moRUDASVCONDTotalScore(Audit):
	mvRUDASVCONDTotalScore = models.BigIntegerField(verbose_name='Visuoconstructional Drawing Total Score', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvRUDASVCONDTotalScore
	class Meta:
		get_latest_by = 'record'
		


class moRUDASJudgementText(Audit):
	mvRUDASJudgementText = models.TextField(verbose_name='Record exactly what patient says and underscore all parts of response which were prompted.', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvRUDASJudgementText
	class Meta:
		get_latest_by = 'record'
		


class moRUDASJudgementTraffic(Audit):
	mvRUDASJudgementTraffic = models.RadioButton(verbose_name='Did person indicate that they would look for traffic?', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvRUDASJudgementTraffic
	class Meta:
		get_latest_by = 'record'
		


class moRUDASJudgementAddSafety(Audit):
	mvRUDASJudgementAddSafety = models.RadioButton(verbose_name='Did person make any additional safety proposals?', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvRUDASJudgementAddSafety
	class Meta:
		get_latest_by = 'record'
		


class moRUDASJudgementTotalScore(Audit):
	mvRUDASJudgementTotalScore = models.BigIntegerField(verbose_name='Judgement Total Score', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvRUDASJudgementTotalScore
	class Meta:
		get_latest_by = 'record'
		


class moRUDASMemoryTea(Audit):
	mvRUDASMemoryTea = models.BooleanField(verbose_name='Tea')
	def __unicode__(self):
		return "%s" % self.mvRUDASMemoryTea
	class Meta:
		get_latest_by = 'record'
		


class moRUDASMemoryOil(Audit):
	mvRUDASMemoryOil = models.BooleanField(verbose_name='Cooking Oil')
	def __unicode__(self):
		return "%s" % self.mvRUDASMemoryOil
	class Meta:
		get_latest_by = 'record'
		


class moRUDASMemoryEggs(Audit):
	mvRUDASMemoryEggs = models.BooleanField(verbose_name='Eggs')
	def __unicode__(self):
		return "%s" % self.mvRUDASMemoryEggs
	class Meta:
		get_latest_by = 'record'
		


class moRUDASMemorySoap(Audit):
	mvRUDASMemorySoap = models.BooleanField(verbose_name='Soap')
	def __unicode__(self):
		return "%s" % self.mvRUDASMemorySoap
	class Meta:
		get_latest_by = 'record'
		


class moRUDASMemoryPrompted(Audit):
	mvRUDASMemoryPrompted = models.BooleanField(verbose_name='Was a prompt given for tea?')
	def __unicode__(self):
		return "%s" % self.mvRUDASMemoryPrompted
	class Meta:
		get_latest_by = 'record'
		


class moRUDASMemoryTotal(Audit):
	mvRUDASMemoryTotal = models.BigIntegerField(verbose_name='Memory Total Score', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvRUDASMemoryTotal
	class Meta:
		get_latest_by = 'record'
		


class moRUDASLangAnimal1(Audit):
	mvRUDASLangAnimal1 = models.CharField(verbose_name='Animal 1', blank=True, null=True, max_length=50)
	def __unicode__(self):
		return "%s" % self.mvRUDASLangAnimal1
	class Meta:
		get_latest_by = 'record'
		


class moRUDASLangAnimal2(Audit):
	mvRUDASLangAnimal2 = models.CharField(verbose_name='Animal 2', blank=True, null=True, max_length=50)
	def __unicode__(self):
		return "%s" % self.mvRUDASLangAnimal2
	class Meta:
		get_latest_by = 'record'
		


class moRUDASLangAnimal3(Audit):
	mvRUDASLangAnimal3 = models.CharField(verbose_name='Animal 3', blank=True, null=True, max_length=50)
	def __unicode__(self):
		return "%s" % self.mvRUDASLangAnimal3
	class Meta:
		get_latest_by = 'record'
		


class moRUDASLangAnimal4(Audit):
	mvRUDASLangAnimal4 = models.CharField(verbose_name='Animal 4', blank=True, null=True, max_length=50)
	def __unicode__(self):
		return "%s" % self.mvRUDASLangAnimal4
	class Meta:
		get_latest_by = 'record'
		


class moRUDASLangAnimal5(Audit):
	mvRUDASLangAnimal5 = models.CharField(verbose_name='Animal 5', blank=True, null=True, max_length=50)
	def __unicode__(self):
		return "%s" % self.mvRUDASLangAnimal5
	class Meta:
		get_latest_by = 'record'
		


class moRUDASLangAnimal6(Audit):
	mvRUDASLangAnimal6 = models.CharField(verbose_name='Animal 6', blank=True, null=True, max_length=50)
	def __unicode__(self):
		return "%s" % self.mvRUDASLangAnimal6
	class Meta:
		get_latest_by = 'record'
		


class moRUDASLangAnimal7(Audit):
	mvRUDASLangAnimal7 = models.CharField(verbose_name='Animal 7', blank=True, null=True, max_length=50)
	def __unicode__(self):
		return "%s" % self.mvRUDASLangAnimal7
	class Meta:
		get_latest_by = 'record'
		


class moRUDASLangAnimal8(Audit):
	mvRUDASLangAnimal8 = models.CharField(verbose_name='Animal 8', blank=True, null=True, max_length=50)
	def __unicode__(self):
		return "%s" % self.mvRUDASLangAnimal8
	class Meta:
		get_latest_by = 'record'
		


class moRUDASLangTotalScr(Audit):
	mvRUDASLangTotalScr = models.BigIntegerField(verbose_name='Language Total Score', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvRUDASLangTotalScr
	class Meta:
		get_latest_by = 'record'
		


class moRUDASTotallScr8(Audit):
	mvRUDASTotallScr8 = models.BigIntegerField(verbose_name='RUDAS Total Score', blank=True, null=True)
	def __unicode__(self):
		return "%s" % self.mvRUDASTotallScr8
	class Meta:
		get_latest_by = 'record'
		

