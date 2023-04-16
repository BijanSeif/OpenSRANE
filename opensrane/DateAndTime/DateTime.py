# /* ****************************************************************** **
# **    OpeSRANE - Open Software for Risk Assessment of Natech Events   **
# **                                                                    **
# **                                                                    **
# **                                                                    **
# ** (C) Copyright 2022, Bijan Sayyafzadeh                              **
# **                                                                    **
# ** All Rights Reserved.                                               **
# **                                                                    **
# ** Commercial use of this program without express permission of the   **
# ** owner (Bijan SayyafZadeh and following Developers), is             **
# ** strictly prohibited.  See file 'COPYRIGHT'  in main directory      **
# ** for information on usage and redistribution,  and for a            **
# ** DISCLAIMER OF ALL WARRANTIES.                                      **
# **                                                                    **
# ** Developed by:                                                      **
# **   Bijan SayyafZadeh (B.Sayyaf@yahoo.com)                           **
# **   MehDi Sharifi                                                    **
# **   Abdolreza Sarvghad Moghaddam                                     **
# **   ----- -----                                                      **
# **                                                                    **
# ** ****************************************************************** */

from opensrane.Misc._NewClass import _NewClass
from .ObjManager import *
import random as _rnd

class DateTime(_NewClass):
    '''
    This Class Defines Date and Time distribution
    
    '''
    Title="Date and Time"

    
    def __init__(self,tag,Day_Night_Ratio=2):
         
        #---- Fix Part for each class __init__ ----
        ObjManager.Add(tag,self)
        _NewClass.__init__(self,tag)
        #------------------------------------------
        
        
        self.name=self.Title
        self.Day_Night_Ratio=Day_Night_Ratio
        
        
        self.wipeAnalysis()
    
    def wipeAnalysis(self):
        # properties that are not constant and amog each analysis will change should be define here
        self.SampledisDay=None
        
        
    def SampleisDay(self):
        
        self.SampledisDay= True if _rnd.random()<self.Day_Night_Ratio/(self.Day_Night_Ratio+1) else False
        
        return self.SampledisDay
        