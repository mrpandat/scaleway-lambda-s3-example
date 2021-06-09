Cette lambda a pour but de migrer les backups de plus d'une semaine vers un bucket différent, pour ne plus surcharger un bucket avec des objets Glacier dont nous n'aurons sûrement jamais besoin.


## Requirements
	
- Install node.js
- Install [Serverless](https://serverless.com) CLI `npm install serverless -g`
- Install node Packages `npm install serverless -g`
- Install all python packages with `pip3 install -r requirements.txt --target ./package`
- You can now deploy the lambda live with `serverless deploy`
- You can see the logs with `serverless logs --function moveoldbackups`
