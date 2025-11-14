class Person:
    def __init__(self, name, privacy, biography):
        self.name = name
        self.privacy = privacy.upper()  
        self.biography = biography

    def getName(self):
        return self.name

    def getPrivacy(self):
        return self.privacy

    def getBiography(self):
        return self.biography
