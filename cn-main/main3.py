import json
import re
import os
import subprocess
import sys
wget_path='/usr/bin/wget'
params={}
for arg in sys.argv[1:]:
 if arg.startswith('--'):
  key_value=arg[len('--'):].split('=')
  if len(key_value)==2:
   key,value=key_value
   params[key]=value
def find_model_json(root_path,mod_json_name):
 for file_name in os.listdir(root_path):
  file_path=os.path.join(root_path,file_name)
  if os.path.isdir(file_path):
   res=find_model_json(file_path,mod_json_name)
   if res is not None:
    return res
  elif file_name==mod_json_name:
   print("find model.json文件：",file_path)
   return file_path
def find_config_json(root_path,config_json_name):
 for file_name in os.listdir(root_path):
  file_path=os.path.join(root_path,file_name)
  if os.path.isdir(file_path):
   res=find_model_json(file_path,config_json_name)
   if res is not None:
    return res
  elif file_name==config_json_name:
   print("find config.json文件：",file_path)
   return file_path
def rec_config_json():
 json_content={"samples_save":True,"samples_format":"png","samples_filename_pattern":"","save_images_add_number":True,"grid_save":True,"grid_format":"png","grid_extended_filename":False,"grid_only_if_multiple":True,"grid_prevent_empty_spots":False,"n_rows":-1,"enable_pnginfo":True,"save_txt":False,"save_images_before_face_restoration":False,"save_images_before_highres_fix":False,"save_images_before_color_correction":False,"jpeg_quality":80,"export_for_4chan":True,"use_original_name_batch":True,"use_upscaler_name_as_suffix":False,"save_selected_only":True,"do_not_add_watermark":False,"temp_dir":"","clean_temp_dir_at_start":False,"outdir_samples":"","outdir_txt2img_samples":"outputs/txt2img-images","outdir_img2img_samples":"outputs/img2img-images","outdir_extras_samples":"outputs/extras-images","outdir_grids":"","outdir_txt2img_grids":"outputs/txt2img-grids","outdir_img2img_grids":"outputs/img2img-grids","outdir_save":"log/images","save_to_dirs":False,"grid_save_to_dirs":False,"use_save_to_dirs_for_ui":False,"directories_filename_pattern":"[date]","directories_max_prompt_words":8,"ESRGAN_tile":192,"ESRGAN_tile_overlap":8,"realesrgan_enabled_models":["R-ESRGAN 4x+","R-ESRGAN 4x+ Anime6B"],"upscaler_for_img2img":None,"face_restoration_model":None,"code_former_weight":0.5,"face_restoration_unload":False,"show_warnings":False,"memmon_poll_rate":8,"samples_log_stdout":False,"multiple_tqdm":True,"print_hypernet_extra":False,"unload_models_when_training":True,"pin_memory":False,"save_optimizer_state":False,"save_training_settings_to_txt":True,"dataset_filename_word_regex":"","dataset_filename_join_string":" ","training_image_repeats_per_epoch":1,"training_write_csv_every":500,"training_xattention_optimizations":False,"training_enable_tensorboard":False,"training_tensorboard_save_images":False,"training_tensorboard_flush_every":120,"sd_model_checkpoint":"","sd_checkpoint_cache":0,"sd_vae_checkpoint_cache":0,"sd_vae":"Automatic","sd_vae_as_default":False,"inpainting_mask_weight":1.0,"initial_noise_multiplier":1.0,"img2img_color_correction":False,"img2img_fix_steps":False,"img2img_background_color":"#ffffff","enable_quantization":False,"enable_emphasis":True,"enable_batch_seeds":True,"comma_padding_backtrack":20,"CLIP_stop_at_last_layers":2,"upcast_attn":False,"use_old_emphasis_implementation":False,"use_old_karras_scheduler_sigmas":False,"use_old_hires_fix_width_height":False,"interrogate_keep_models_in_memory":False,"interrogate_return_ranks":False,"interrogate_clip_num_beams":1,"interrogate_clip_min_length":24,"interrogate_clip_max_length":48,"interrogate_clip_dict_limit":1500,"interrogate_clip_skip_categories":[],"interrogate_deepbooru_score_threshold":0.7,"deepbooru_sort_alpha":False,"deepbooru_use_spaces":False,"deepbooru_escape":True,"deepbooru_filter_tags":"","extra_networks_default_view":"thumbs","extra_networks_default_multiplier":1.0,"sd_hypernetwork":"None","return_grid":False,"do_not_show_images":False,"add_model_hash_to_info":True,"add_model_name_to_info":True,"disable_weights_auto_swap":True,"send_seed":True,"send_size":True,"font":"","js_modal_lightbox":True,"js_modal_lightbox_initially_zoomed":True,"show_progress_in_title":True,"samplers_in_dropdown":False,"dimensions_and_batch_together":True,"keyedit_precision_attention":0.1,"keyedit_precision_extra":0.05,"quicksettings":"sd_model_checkpoint, sd_vae, CLIP_stop_at_last_layers, use_old_karras_scheduler_sigmas, always_discard_next_to_last_sigma","ui_reorder":"inpaint, sampler, checkboxes, hires_fix, dimensions, cfg, seed, batch, override_settings, scripts","ui_extra_networks_tab_reorder":"","localization":"zh_CN","show_progressbar":True,"live_previews_enable":True,"show_progress_grid":True,"show_progress_every_n_steps":20,"show_progress_type":"Approx NN","live_preview_content":"Prompt","live_preview_refresh_period":1000,"hide_samplers":[],"eta_ddim":0.0,"eta_ancestral":1.0,"ddim_discretize":"uniform","s_churn":0.0,"s_tmin":0.0,"s_noise":1.0,"eta_noise_seed_delta":31337,"always_discard_next_to_last_sigma":False,"postprocessing_enable_in_main_ui":[],"postprocessing_operation_order":[],"upscaling_max_images_in_cache":5,"disabled_extensions":[],"sd_checkpoint_hash":"7af57400eb7303877ec35e5b9e03fc29802c44066828165dc3a20b973c439428","ldsr_steps":100,"ldsr_cached":False,"SWIN_tile":192,"SWIN_tile_overlap":8,"sd_lora":"None","lora_apply_to_outputs":False,"tac_tagFile":"danbooru.csv","tac_active":True,"tac_activeIn.txt2img":True,"tac_activeIn.img2img":True,"tac_activeIn.negativePrompts":True,"tac_activeIn.thirdParty":True,"tac_activeIn.modelList":"","tac_activeIn.modelListMode":"Blacklist","tac_maxResults":15.0,"tac_showAllResults":False,"tac_resultStepLength":100.0,"tac_delayTime":100.0,"tac_useWildcards":True,"tac_useEmbeddings":True,"tac_useHypernetworks":True,"tac_useLoras":True,"tac_showWikiLinks":False,"tac_replaceUnderscores":True,"tac_escapeParentheses":True,"tac_appendComma":True,"tac_alias.searchByAlias":True,"tac_alias.onlyShowAlias":False,"tac_translation.translationFile":"CN.csv","tac_translation.oldFormat":True,"tac_translation.searchByTranslation":True,"tac_extra.extraFile":"extra-quality-tags.csv","tac_extra.addMode":"Insert before","additional_networks_extra_lora_path":"","additional_networks_sort_models_by":"name","additional_networks_reverse_sort_order":False,"additional_networks_model_name_filter":"","additional_networks_xy_grid_model_metadata":"","additional_networks_hash_thread_count":1.0,"additional_networks_back_up_model_when_saving":True,"additional_networks_show_only_safetensors":False,"additional_networks_show_only_models_with_metadata":"disabled","additional_networks_max_top_tags":20.0,"additional_networks_max_dataset_folders":20.0,"images_history_preload":False,"images_record_paths":True,"images_delete_message":True,"images_history_page_columns":6.0,"images_history_page_rows":6.0,"images_history_pages_perload":20.0,"img_downscale_threshold":4.0,"target_side_length":4000.0,"no_dpmpp_sde_batch_determinism":False,"control_net_max_models_num":3}
 if params["image"]=="True":
  json_content["outdir_txt2img_samples"]="/content/drive/MyDrive/outputs/txt2img-images"
  json_content["outdir_img2img_samples"]="/content/drive/MyDrive/outputs/img2img-images"
  json_content["outdir_extras_samples"]="/content/drive/MyDrive/outputs/extras-images"
  json_content["outdir_txt2img_grids"]="/content/drive/MyDrive/outputs/txt2img-grids"
  json_content["outdir_img2img_grids"]="/content/drive/MyDrive/outputs/img2img-grids"
 with open(f'{params["dir"]}/config.json','w')as configFile:
  json.dump(json_content,configFile,ensure_ascii=False,indent=4)
if params["config"]=="False":
 rec_config_json()
else:
 res_config_json=find_config_json('/content/drive/','config.json')
 print(res_config_json)
 subprocess.run(f'cp {res_config_json} {params["dir"]}/config.json',shell=True)
if params["download"]=="True":
 subprocess.run([wget_path,'-O',f'{params["dir"]}/javascript/png_auto_download.js','https://github.com/s4afa451dgf415f/colab_stable_diffusion/raw/main/png_auto_download.js'],check=True)
else:
 if os.path.exists(f'{params["dir"]}/javascript/png_auto_downloadjs'):
  os.remove(f'{params["dir"]}/javascript/png_auto_download.js')
if params["ui"]=="anapnoe手机端完美适配":
 subprocess.run([wget_path,'-O',f'{params["dir"]}/javascript/PNG_info_web.js','https://github.com/s4afa451dgf415f/colab_stable_diffusion/raw/main/PNG_info_web.js'],check=True)
 with open(f'{params["dir"]}/modules/ui.py','r')as readFile:
  content=readFile.read()
 content=content.replace('''                for tabname, button in buttons.items():
                    parameters_copypaste.register_paste_params_button(parameters_copypaste.ParamBinding(
                        paste_button=button, tabname=tabname, source_text_component=generation_info, source_image_component=image,
                    ))
        image.change(
            fn=wrap_gradio_call(modules.extras.run_pnginfo),
            inputs=[image],
            outputs=[html, generation_info, html2],
        )''','')
 with open(f'{params["dir"]}/modules/ui.py','w')as writeFile:
  writeFile.write(content)
 with open(f'{params["dir"]}/javascript/PNG_info_web.js','r')as readFile:
  content=readFile.read()
 content=content.replace('''querySelector("#tab_pnginfo > div > div > div:nth-child(2) > div:nth-child(3)")''','querySelector("#tab_pnginfo > div > div>div>div:nth-child(4)")')
 with open(f'{params["dir"]}/javascript/PNG_info_web.js','w')as writeFile:
  writeFile.write(content)
else:
 css_content='''
  @media screen and (max-width: 600px) {
    .gradio-slider input[type="range"]{
      display: none;
    }
    .gradio-slider input[type="number"]{
      width: 18em;
  }
  }
  '''
 with open(f'{params["dir"]}/style.css','a')as cssFile:
  cssFile.write(css_content)
 subprocess.run([wget_path,'-O',f'{params["dir"]}/javascript/PNG_info_web.js','https://github.com/s4afa451dgf415f/colab_stable_diffusion/raw/main/PNG_info_web.js'],check=True)
 with open(f'{params["dir"]}/modules/ui.py','r')as readFile:
  content=readFile.read()
 content=content.replace('''                for tabname, button in buttons.items():
                    parameters_copypaste.register_paste_params_button(parameters_copypaste.ParamBinding(
                        paste_button=button, tabname=tabname, source_text_component=generation_info, source_image_component=image,
                    ))
        image.change(
            fn=wrap_gradio_call(modules.extras.run_pnginfo),
            inputs=[image],
            outputs=[html, generation_info, html2],
        )''','')
 with open(f'{params["dir"]}/modules/ui.py','w')as writeFile:
  writeFile.write(content)

#import zlib, base64
#exec(zlib.decompress(base64.b64decode('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')))
# Created by pyminifier (https://github.com/dzhuang/pyminifier3)
