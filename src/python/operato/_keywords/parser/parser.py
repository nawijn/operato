from pyparsing import Literal
import pyparsing  # make sure you have this installed
import pathlib
import os
import re
import glob


class hm_parser:

    def __init__(self, fileName):
        with open(fileName, 'r') as r:
            self.file = r.read()
        self.format()
        self.default()
        self.attributes()

    def convertDictionary(self, code):
        "It converts the equality in text file to the dictionary"
        dictinory = {}
        for i in code.split(";\n"):
            try:
                a, b = i.split("=")
                dictinory[a.strip()] = eval(b.strip())
            except:
                pass
        return dictinory

    def format(self):
        # Not working in some files
        # fmts = re.search(
        #     r"(FORMAT.*\s*(\{(\s.*\s)*\}))", self.file, re.M).group(0)
        loc = self.file.find("FORMAT")
        opBrace = self.file.find("{", loc)
        clBrace = True
        counter = opBrace+1
        insidebrace = 0
        while clBrace:
            if self.file[counter] == "{":
                # TODO get the relations for conditional cards
                insidebrace += 1
            elif self.file[counter] == "}" and insidebrace > 0:
                insidebrace -= 1
            elif self.file[counter] == "}" and insidebrace == 0:
                clBrace = False
            counter += 1
        # to get format text in the file
        fmts = self.file[loc:counter]

        self.fmts = {}

        # for fmt in fmts: #It is for getting other versions of cards
        self.fmts["HEADER"] = re.search(
            r"HEADER\((.*)\)", fmts, re.M).group(1)
        self.fmts["VERSION"] = re.search(
            "FORMAT\((.*)\)", fmts, re.M).group(1)
        CARDS = re.findall(r'CARD\("(.*);', fmts, re.M)
        COMMENTS = re.findall(
            r"COMMENT\((.*)\)", fmts, re.M)
        self.fmts["STRACTURE"]=""
        self.fmts["VARIABLE"]=[]
        for i,card in enumerate(CARDS):
            if i>0:
                self.fmts["STRACTURE"]+="\t\t\t"+COMMENTS[i-1]+",\n"

            data=card.split('",')
            self.fmts["STRACTURE"]+='\t\t\t"'+data[0]+'"%('+data[1]+",\n"
            for var in data[1].replace(")","").split(","):
                self.fmts["VARIABLE"].append(var.strip())
            
    def default(self):
        dflt = re.search(
            "DEFAULTS[^{]*\{([^}]+)\}", self.file, re.M).group(1)
        self.dflt = self.convertDictionary(dflt)


    def attributes(self):
        attr = re.search(
            "ATTRIBUTES[^{]*\{([^}]+)\}", self.file, re.M).group(1)
        self.attr=""
        for element in attr.split(";"):
            for i,member in enumerate(element.split("=")):
                if i%2==0:
                      self.attr+="\t"+member.strip()
                else:
                    self.attr+=self.typeConverter(member.strip())+"\n"
                    
    def typeConverter(self,text):
        if "FLOAT" in text:
            comm1=text.find('"')
            comm2=text.find('"',comm1+1)
            return f":float\t\t\t#{text[comm1+1:comm2]}"
        elif "INT" in text:
            comm1=text.find('"')
            comm2=text.find('"',comm1+1)
            return f":int\t\t\t#{text[comm1:comm2]}"
        elif "STRING" in text:
            comm1=text.find('"')
            comm2=text.find('"',comm1+1)
            return f":str\t\t\t#{text[comm1:comm2]}"
        else:
            return f"\t\t\t\t#{text}"

class generator:
    def __init__(self, fileName, ParsedObject):
        fileName = fileName.replace(".cfg", "")
        self.file = fileName
        p = pathlib.Path(fileName)
        self.onedir = os.path.join(*p.parts[-2:])
        self.Name = self.onedir.replace("/", "")
        self.data = ParsedObject

        self.readmaster()
        self.replace()
        self.createDataclass()

    def readmaster(self):
        with open("master.py", "r") as master:
            self.code = master.read()

    def replace(self):
        # define desired replacements here
        variables=self.data.fmts["VARIABLE"]
        for default in self.data.dflt.items():
            if default[0] in variables:
                variables.remove(default[0])
                variables.append(default[0]+"="+str(default[1]))
        inputs=""
        for var in variables:
            inputs+=" "+ var+","
        rep = {"$NAME": self.Name, "$ATTRIBUTES": self.data.attr,
               "$FORMAT": self.data.fmts["STRACTURE"], "$KEYWORD": self.onedir, "$VARIABLE":inputs}
        rep = dict((re.escape(k), v) for k, v in rep.items())
        pattern = re.compile("|".join(rep.keys()))
        self.code = pattern.sub(
            lambda m: rep[re.escape(m.group(0))], self.code)

    def createDataclass(self):
        with open(f"{self.Name}.py", "w") as product:
            product.write(self.code)


def files():
    filenames = []
    for file in glob.glob(os.getcwd()+'/**/*.cfg', recursive=True):
        filenames.append(file)
    return filenames


# The code is written for example case of LAW90.cfg"
fileNames = files()
for cfg in fileNames:
    parsed = hm_parser(cfg)
    generator(cfg, parsed)
