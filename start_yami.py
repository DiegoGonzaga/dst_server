import os
cluster="yami"
os.chdir("/home/diego-gonzaga/.local/share/Steam/steamapps/common/Don't Starve Together Dedicated Server/bin/")
command = f"./dontstarve_dedicated_server_nullrenderer -console -cluster {cluster} -shard"
shard = "Master"
os.system(f"gnome-terminal -- {command} {shard}")
shard = "Caves"
os.system(f"gnome-terminal -- {command} {shard}")
