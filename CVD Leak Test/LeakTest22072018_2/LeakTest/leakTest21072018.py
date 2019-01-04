from qrystal import Recipe

####------------     Example of an error free recipe    ------------####

def evac():

	global recipe
	global last_time

	recipe.chss_ctrl_pump_on (begin_time = last_time)
	last_time = recipe.last_end_time()

	recipe.chss_ctrl_pump_off (begin_time = last_time + 3 * 60)
	last_time = recipe.last_end_time()


def flush():

	global recipe
	global last_time

	recipe.mfc_flush_on (begin_time = last_time, chn_idx = 2)
	last_time = recipe.last_end_time()

	recipe.mfc_flush_off (begin_time = last_time + 2 * 60, chn_idx = 2)
	last_time = recipe.last_end_time()

def evac_n_flush():

	evac()
	flush()

def evacmax():

	global recipe
	global last_time

	recipe.chss_ctrl_pump_on (begin_time = last_time)
	last_time = recipe.last_end_time()

	recipe.chss_ctrl_pump_off (begin_time = last_time + 30 * 60)
	last_time = recipe.last_end_time()


''' -------------------------------------------- '''


recipe = Recipe()
last_time = recipe.last_end_time()
recipe.system_initialize (begin_time=last_time)

evac_n_flush()
evac_n_flush()

evacmax()

recipe.credential ('samim', 'leakTest_21072018')
recipe.run()
