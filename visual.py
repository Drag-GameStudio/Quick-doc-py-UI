import eel
import backend

@eel.expose
def get_info():
    dh = backend.DataHandler()
    langs = dh.support_languages()
    versions = dh.support_versions()
    data = {
        "languages": langs,
        "versions": versions
    }

    return data

@eel.expose
def gen_doc(name: str, root_dir: str, 
            ignore: list[str], languages: list[str],
            g_prompt: str, d_prompt: str, 
            version: str):
    

    ad = backend.AutoDock(name_project=name, root_dir=root_dir, 
                     ignore=ignore, languages=languages,
                     general_prompt=g_prompt, default_prompt=d_prompt,
                     gpt_version=version)
    
    ad.gen_doc()

eel.init("GUI")

eel.start("index.html", port=809, size=(400, 300), mode="chrome")