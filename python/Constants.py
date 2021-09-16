SCALE_FACTOR_FROM_DBF = 3000000             #ratio to scale the DBF / shape file by
SR_POST_POST_WIDTH = 6                      #width between posts for solar farm rows
SR_MODULE_HEIGHT = 2                      #height of the solar module used
SR_END_DELTA = 0.1                          #set-back from edge of farm boundary for first row
SR_END_END_WIDTH = 0.5                        #spacing between ends of rows
SR_ROW_LENGTHS = [88, 60, 32]               #roughly nx horizon
SR_NUM_MODULES_PER_ROW = [84, 56, 28]       #roughly nx horizon
SR_ROADWAY_WIDTH = 8                        #roadway width (not road width) between rows
SF_SETBACK = 10                             #solar farm boundary setback
VERBOSE = True                              #print all output
DEBUG = True                                #print lots of output
ROAD_Y_DELTA = 1  #temp see if new line idea works
SPIKE_MIN = 10
MAX_ROAD_DELTA_ANGLE = 50
ROAD_DELTA = 1  #additional offset between top of row and row marker
FIRST_ROW_1LONG_ROAD = False #if True, first row is NOT 2x long, just 1x long then road
#TODO implement some way to store 'road every second long row'