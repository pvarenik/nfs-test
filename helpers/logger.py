import ConfigParser


class Log():
    def __init__(self):
        Config = ConfigParser.ConfigParser()
        Config.read("../config.cfg")
        self.log_file = Config.get('PARAMETERS', 'LOG_FILE')

    def log_line(self, line):
        f = open(self.log_file, 'a')
        f.write(line + "\n")
        f.close()

    def clear_log(self):
        f = open(self.log_file, 'w+')
        f.close()
