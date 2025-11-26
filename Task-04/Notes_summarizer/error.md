
────────────────────────── Traceback (most recent call last) ───────────────────────────
  E:\Documents\gemini_cli\class_content\AIDD 30 day                                     
  challenge\Task-04\Notes_summarizer\.venv\Lib\site-packages\streamlit\runtime\scriptr  
  unner\exec_code.py:129 in exec_func_with_error_handling                               
                                                                                        
  E:\Documents\gemini_cli\class_content\AIDD 30 day                                     
  challenge\Task-04\Notes_summarizer\.venv\Lib\site-packages\streamlit\runtime\scriptr  
  unner\script_runner.py:669 in code_to_exec                                            
                                                                                        
  E:\Documents\gemini_cli\class_content\AIDD 30 day                                     
  challenge\Task-04\Notes_summarizer\app.py:12 in <module>                              
                                                                                        
      9 sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.'  
     10                                                                                 
     11 # Import agent and tools (will uncomment as they become fully functional)       
  ❱  12 from agent import main as run_agent                                             
     13 from tools import (                                                             
     14 │   extract_text_from_pdf, extract_text_from_pptx, extract_text_from_docx,      
     15 │   extract_text_from_csv, extract_text_from_image, get_youtube_transcript_and  
                                                                                        
  E:\Documents\gemini_cli\class_content\AIDD 30 day                                     
  challenge\Task-04\Notes_summarizer\agent.py:7 in <module>                             
                                                                                        
      4 from dotenv import load_dotenv                                                  
      5                                                                                 
      6 # Import the tools from tools.py                                                
  ❱   7 from tools import (                                                             
      8 │   read_user_profile, update_user_profile, add_to_rag_memory, retrieve_from_r  
      9 )                                                                               
     10                                                                                 
                                                                                        
  E:\Documents\gemini_cli\class_content\AIDD 30 day                                     
  challenge\Task-04\Notes_summarizer\tools.py:6 in <module>                             
                                                                                        
      3 import docx                                                                     
      4 import pandas as pd                                                             
      5 from PIL import Image                                                           
  ❱   6 import easyocr                                                                  
      7 import yt_dlp                                                                   
      8 # import whisper # Commented out due to potential high dependency               
      9 import os                                                                       
                                                                                        
  E:\Documents\gemini_cli\class_content\AIDD 30 day                                     
  challenge\Task-04\Notes_summarizer\.venv\Lib\site-packages\easyocr\__init__.py:1 in   
  <module>                                                                              
                                                                                        
  ❱ 1 from .easyocr import Reader                                                       
    2                                                                                   
    3 __version__ = '1.7.2'                                                             
    4                                                                                   
                                                                                        
  E:\Documents\gemini_cli\class_content\AIDD 30 day                                     
  challenge\Task-04\Notes_summarizer\.venv\Lib\site-packages\easyocr\easyocr.py:3 in    
  <module>                                                                              
                                                                                        
      1 # -*- coding: utf-8 -*-                                                         
      2                                                                                 
  ❱   3 from .recognition import get_recognizer, get_text                               
      4 from .utils import group_text_box, get_image_list, calculate_md5, get_paragrap  
      5 │   │   │   │      download_and_unzip, printProgressBar, diff, reformat_input,  
      6 │   │   │   │      make_rotated_img_list, set_result_with_confidence,\          
                                                                                        
  E:\Documents\gemini_cli\class_content\AIDD 30 day                                     
  challenge\Task-04\Notes_summarizer\.venv\Lib\site-packages\easyocr\recognition.py:2   
  in <module>                                                                           
                                                                                        
      1 from PIL import Image                                                           
  ❱   2 import torch                                                                    
      3 import torch.backends.cudnn as cudnn                                            
      4 import torch.utils.data                                                         
      5 import torch.nn.functional as F                                                 
                                                                                        
  E:\Documents\gemini_cli\class_content\AIDD 30 day                                     
  challenge\Task-04\Notes_summarizer\.venv\Lib\site-packages\torch\__init__.py:281 in   
  <module>                                                                              
                                                                                        
     278 │   │                                                                          
     279 │   │   kernel32.SetErrorMode(prev_error_mode)                                 
     280 │                                                                              
  ❱  281 │   _load_dll_libraries()                                                      
     282 │   del _load_dll_libraries                                                    
     283                                                                                
     284                                                                                
                                                                                        
  E:\Documents\gemini_cli\class_content\AIDD 30 day                                     
  challenge\Task-04\Notes_summarizer\.venv\Lib\site-packages\torch\__init__.py:264 in   
  _load_dll_libraries                                                                   
                                                                                        
     261 │   │   │   │   │   err.strerror += (                                          
     262 │   │   │   │   │   │   f' Error loading "{dll}" or one of its dependencies.'  
     263 │   │   │   │   │   )                                                          
  ❱  264 │   │   │   │   │   raise err                                                  
     265 │   │   │   │   elif res is not None:                                          
     266 │   │   │   │   │   is_loaded = True                                           
     267 │   │   │   if not is_loaded:                                                  
────────────────────────────────────────────────────────────────────────────────────────
OSError: [WinError 1114] A dynamic link library (DLL) initialization routine failed.
Error loading "E:\Documents\gemini_cli\class_content\AIDD 30 day 
challenge\Task-04\Notes_summarizer\.venv\Lib\site-packages\torch\lib\c10.dll" or one of
its dependencies.

OSError: [WinError 1114] A dynamic link library (DLL) initialization routine failed. Error loading "E:\Documents\gemini_cli\class_content\AIDD 30 day challenge\Task-04\Notes_summarizer\.venv\Lib\site-packages\torch\lib\c10.dll" or one of its dependencies.

File "E:\Documents\gemini_cli\class_content\AIDD 30 day challenge\Task-04\Notes_summarizer\.venv\Lib\site-packages\streamlit\runtime\scriptrunner\exec_code.py", line 129, in exec_func_with_error_handling
    result = func()
File "E:\Documents\gemini_cli\class_content\AIDD 30 day challenge\Task-04\Notes_summarizer\.venv\Lib\site-packages\streamlit\runtime\scriptrunner\script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^
File "E:\Documents\gemini_cli\class_content\AIDD 30 day challenge\Task-04\Notes_summarizer\app.py", line 12, in <module>
    from agent import main as run_agent
File "E:\Documents\gemini_cli\class_content\AIDD 30 day challenge\Task-04\Notes_summarizer\agent.py", line 7, in <module>
    from tools import (
        read_user_profile, update_user_profile, add_to_rag_memory, retrieve_from_rag_memory
    )
File "E:\Documents\gemini_cli\class_content\AIDD 30 day challenge\Task-04\Notes_summarizer\tools.py", line 6, in <module>
    import easyocr
File "E:\Documents\gemini_cli\class_content\AIDD 30 day challenge\Task-04\Notes_summarizer\.venv\Lib\site-packages\easyocr\__init__.py", line 1, in <module>
    from .easyocr import Reader
File "E:\Documents\gemini_cli\class_content\AIDD 30 day challenge\Task-04\Notes_summarizer\.venv\Lib\site-packages\easyocr\easyocr.py", line 3, in <module>
    from .recognition import get_recognizer, get_text
File "E:\Documents\gemini_cli\class_content\AIDD 30 day challenge\Task-04\Notes_summarizer\.venv\Lib\site-packages\easyocr\recognition.py", line 2, in <module>
    import torch
File "E:\Documents\gemini_cli\class_content\AIDD 30 day challenge\Task-04\Notes_summarizer\.venv\Lib\site-packages\torch\__init__.py", line 281, in <module>
    _load_dll_libraries()
    ~~~~~~~~~~~~~~~~~~~^^
File "E:\Documents\gemini_cli\class_content\AIDD 30 day challenge\Task-04\Notes_summarizer\.venv\Lib\site-packages\torch\__init__.py", line 264, in _load_dll_libraries
    raise err