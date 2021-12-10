from Text_Editor_using_Python.tkeditor import Editor

if __name__=="__main__":
    sk=Editor("SKSINGH-EDITOR","600x500")
    sk.Createtextarea()
    sk.createMenu("file")
    sk.createSubMenu("New File",sk.newfile)
    sk.createSubMenu("Open File",sk.openfile)
    sk.createSubMenu("Save File",sk.savefile)
    sk.createSubMenu("exit",sk.exitfile)
    sk.createMenu("edit")
    sk.createSubMenu("copy",sk.copy)
    sk.createSubMenu("cut",sk.cut)
    sk.createSubMenu("paste",sk.paste)
    sk.createMenu("view")
    sk.createSubmenuForFontSize("Change Font Size")
    sk.createMenu("help")
    sk.createSubMenu("about",sk.about)
    sk.ShowGUI()


