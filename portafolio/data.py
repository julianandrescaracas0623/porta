import json

class Media:
    def __init__(self, email, cv, github, linkedin):
        self.email = email
        self.cv = cv
        self.github = github
        self.linkedin = linkedin

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

class Technology:
    def __init__(self, icon, name):
        self.icon = icon
        self.name = name

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

class Info:
    def __init__(self, icon, title, subtitle, description, date="", certificate="", technologies=None, image="", url="", github=""):
        self.icon = icon
        self.title = title
        self.subtitle = subtitle
        self.description = description
        self.date = date
        self.certificate = certificate
        self.technologies = [Technology.from_dict(t) for t in technologies] if technologies else []
        self.image = image
        self.url = url
        self.github = github

    @classmethod
    def from_dict(cls, data):
        return cls(
            icon=data.get("icon"),
            title=data.get("title"),
            subtitle=data.get("subtitle"),
            description=data.get("description"),
            date=data.get("date", ""),
            certificate=data.get("certificate", ""),
            technologies=data.get("technologies", []),
            image=data.get("image", ""),
            url=data.get("url", ""),
            github=data.get("github", "")
        )

class Extra:
    def __init__(self, title, description, image, url):
        self.title = title
        self.description = description
        self.image = image
        self.url = url

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

class Data:
    def __init__(self, avatar, name, title, location, media, about, technologies, experience, projects, training, extras):
        self.avatar = avatar
        self.name = name
        self.title = title
        self.location = location
        self.media = Media.from_dict(media)
        self.about = about
        self.technologies = [Technology.from_dict(t) for t in technologies]
        self.experience = [Info.from_dict(info_dict) for info_dict in experience]
        self.projects = [Info.from_dict(info_dict) for info_dict in projects]
        self.training = [Info.from_dict(info_dict) for info_dict in training]
        self.extras = [Extra.from_dict(info) for info in extras]

# Cargar los datos del JSON y crear una instancia de Data
with open("assets/data/data.json") as file:
    json_data = json.load(file)

data = Data(**json_data)
