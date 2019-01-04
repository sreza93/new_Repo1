from qrystal import Recipe

####------------     Example of an error free recipe    ------------####

def evac():

	global recipe
	global last_time

	recipe.chss_ctrl_pump_on (begin_time = last_time)
	last_time = recipe.last_end_time()

	recipe.chss_ctrl_pump_off (begin_time = last_time + 1 * 60)
	last_time = recipe.last_end_time()


def flush():

	global recipe
	global last_time

	recipe.mfc_flush_on (begin_time = last_time, chn_idx = 2)
	last_time = recipe.last_end_time()

	recipe.mfc_flush_off (begin_time = last_time + 1 * 60, chn_idx = 2)
	last_time = recipe.last_end_time()

def evac_n_flush():

	evac()
	flush()

def evacmax():

	global recipe
	global last_time

	recipe.chss_ctrl_pump_on (begin_time = last_time)
'''---------------------------------------------------------------'''
def init_ramp():

	global recipe
	global last_time

	recipe.tcon_initialize_ramps (begin_time = last_time)
	recipe.tcon_mains_switch_on (begin_time = last_time)
	last_time = recipe.last_end_time()


def fini_ramp():
	global recipe
	global last_time

	recipe.tcon_mains_switch_off (begin_time = last_time)
	last_time = recipe.last_end_time()
'''---------------------------------------------------------'''
	
def heat100():

	global recipe
	global last_time

	recipe.tcon_begin_linear_ramps (
		begin_time=last_time, zone_idx_list = [0,1,2,3,4,5,6,7,8,9,10,11],
		end_temp_deg_C = 100, duration = "00:10:00")

	last_time = recipe.last_end_time()

def heat200():

	global recipe
	global last_time

	recipe.tcon_begin_linear_ramps (
		begin_time=last_time, zone_idx_list = [1,2,3,4,5,6,7,8,9,10],
		end_temp_deg_C = 200, duration = "00:10:00")

	last_time = recipe.last_end_time()

        recipe.tcon_begin_linear_ramps (
		begin_time=last_time, zone_idx_list = [0,1,2,3,4,5,6,7,8,9,10,11],
		end_temp_deg_C = 100, duration = "00:30:00")

	last_time = recipe.last_end_time()

''' -------------------------------------------- '''


recipe = Recipe()
last_time = recipe.last_end_time()
recipe.system_initialize (begin_time=last_time)

evac_n_flush()
evac_n_flush()

evacmax()
init_ramp()

heat100()
heat200()

fini_ramp()

recipe.credential ('samim', 'leakTest_21072018_2')
recipe.run()
