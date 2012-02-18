def main(buildout, data, workspace):
    missing = []
    for profile in data['profiles.csv']:
        if not profile['PROJECTID'] in buildout['project_users']:
            missing.append(profile['PROJECTID'])
    if missing:
        message = []
        message.append("Add a user for the project in the project_users section:")
        message.append("[project_users]")
        for project in missing:
            message.append("%s = anonymous" % project)
        raise AttributeError("Missing configuration\n%s" % "\n".join(message))
    