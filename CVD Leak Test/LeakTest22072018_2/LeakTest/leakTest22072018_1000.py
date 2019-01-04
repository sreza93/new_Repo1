from qrystal import Recipe

recipe = Recipe()
last_time = recipe.last_end_time()

recipe.system_initialize (begin_time = last_time)
recipe.tcon_initialize_ramps (begin_time = last_time)

recipe.chss_ctrl_pump_on (begin_time = last_time)
recipe.tcon_mains_switch_on (begin_time = last_time)

last_time = recipe.last_end_time()


'''-------------------------------------------------------'''

recipe.tcon_begin_linear_ramps (
	begin_time = last_time, zone_idx_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
	end_temp_deg_C = 1000, duration = "00:50:00")

recipe.mfc_set_flow_rate_sccm (
		begin_time = last_time, chn_idx = 2, flow_rate = 20)


last_time = recipe.last_end_time()

recipe.tcon_begin_linear_ramps (
	begin_time = last_time, zone_idx_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
	end_temp_deg_C = 1000, duration = "00:10:00")

last_time = recipe.last_end_time()
recipe.mfc_set_flow_rate_sccm (
		begin_time = last_time, chn_idx = 2, flow_rate = 0)
'''---------------------------------------------------------------------'''

recipe.tcon_mains_switch_off (begin_time = last_time)

recipe.credential ('samim', 'LeakTest22072018_2')
recipe.run()
