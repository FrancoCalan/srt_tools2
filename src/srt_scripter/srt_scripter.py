import argparse
import io

class SrtScripter():
    """
    Generic SRT scripter with common functions for SRT operation.
    """
    def __init__(self):
        self.parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        self.add_parser_arguments()
        self.args = self.parser.parse_args()

        self.scriptname = self.args.output 
        if not self.scriptname.endswith(".cmd"): # add .cmd extension if not present
            self.scriptname + ".cmd"

        self.script = io.open(self.scriptname, "w", newline='\r\n') # using Windows newline

    def add_parser_arguments(self):
        """
        Add standard parser argments to the scripter.
        """
        self.parser.add_argument("-o", "--output", type=str, default="script.cmd",
            help="The script file name generated by the scripter.")
        self.parser.add_argument("-r", "--rad", type=str, default="",
            help="Name of the .rad file where the script with write the measured data.")
        self.parser.add_argument("-f", "--freq", type=int, default=1420,
            help="Center frequency for calibration and measurements.")
        self.parser.add_argument("-m", "--mode", type=int, default=1,
            help="Receptor mode.") #TODO add mode explanations, add mode limits
        self.parser.add_argument("-ca", "--cal_az", type=float, default=200,
            help="Azimuth position for calibration.")
        self.parser.add_argument("-ce", "--cal_el", type=float, default=30,
            help="Elevation position for calibration.")
        
    # basic command write functions
    def write_record(self):
        self.script.write(u': record ' + self.args.rad + '\n')

    def write_roff(self):
        self.script.write(u': roff\n')

    def write_freq(self):
        self.script.write(u': freq ' + str(self.args.freq) + ' ' + str(self.args.mode) + '\n')

    def write_noisecal(self):
        self.script.write(u': noisecal\n')

    def write_azel(self, az, el, delay=0):
        delay = self.blank_zero_delay(delay)
        self.script.write(u':' + str(delay) + ' azel ' + str(az) + ' '+ str(el) + '\n')
    
    def write_offset(self, az, el, delay=0):
        delay = self.blank_zero_delay(delay)
        self.script.write(u':' + str(delay) + ' offset ' + str(az) + ' ' + str(el) + '\n')

    def write_source(self, source, delay=0):
        delay = self.blank_zero_delay(delay)
        self.script.write(u':' + str(delay) + ' ' + source + '\n')

    def write_stow(self):
        self.script.write(u': stow\n')

    # composite write functions
    def write_calibration(self):
        self.write_azel(self.args.cal_az, self.args.cal_el)
        self.write_freq()
        self.write_noisecal()

    # others
    def close(self):
        self.script.close()
    
    def blank_zero_delay(self, delay):
        """
        If delay is 0, don't write delay.
        """
        if delay == 0:
            return ''
        return delay
