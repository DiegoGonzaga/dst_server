cd "C:\steamcmd\steamapps\common\Don't Starve Together Dedicated Server\bin"
set cluster=yami
start "Master - %cluster%" dontstarve_dedicated_server_nullrenderer -console -cluster %cluster% -shard Master
start "Caves - %cluster%" dontstarve_dedicated_server_nullrenderer -console -cluster %cluster% -shard Caves