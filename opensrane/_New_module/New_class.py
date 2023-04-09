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

class New_class(_NewClass):
    
    
    def __init__(self,tag):
         
        #---- Fix Part for each class __init__ ----
        ObjManager.Add(tag,self)
        _NewClass.__init__(self,tag)
        #------------------------------------------
        
        
        
    pass