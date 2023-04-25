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
# **   Bijan SayyafZadeh (OpenSRANE@Gmail.com)                           **
# **   MehDi Sharifi                                                    **
# **   Abdolreza S. Moghadam                                     **
# **   Eslam Kashi                                                      **
# **                                                                    **
# ** ****************************************************************** */

class _GlobalParameters():
    '''
    In this Global Parameters that any plant unit should have and the other 
    Classes and functyions and ... use them
    '''
    
    def __init__(self):
        
        
        
        self.wipeAnalysis()
                
    def wipeAnalysisGlobal(self):
        pass

    def wipeAnalysis(self):
        self.wipeAnalysisGlobal()
        pass          
    