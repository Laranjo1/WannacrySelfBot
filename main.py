# Biblioteca padrão (built-in)
import os
import threading
import subprocess
import random
import re
import json
import asyncio

# Bibliotecas de terceiros (3rd party)
import discord
import aiohttp
import requests

from discord.ext import commands
from colorama import Fore

# Módulos locais
from keep_alive import keep_alive

respondidos = []
grupos = []
notperm = []

afkold = None
afkb4 = None

afkb3 = False
afkb2 = False

emojis1 = None
presence1 = False

statuschanger = False
calldetector = False
status1 = False
infinite1 = False

switch1 = False
anihype1 = False
changer1 = False
purge0 = False
purge1 = False

my_secret6 = os.getenv("token")
client = commands.Bot(command_prefix='$', self_bot=True, help_command=None)

heads = [
  {
      "Content-Type": "application/json",
      'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0'
  }]
def geek(token=None):
  headers = random.choice(heads)
  if token:
      headers.update({"Authorization": token})
  return headers

def cls():
  os.system('cls' if os.name=='nt' else 'clear')  

@client.event
async def on_ready():
  global calldetector, statuschanger, presence1, grupos
  tasks = []
  await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Streaming(platform='Left',name=f'.gg/wannacry', url=f'https://www.youtube.com/watch?v=3C6smbJdKyY'))
  tasks.append(asyncio.create_task(ante_queda()))
  cls()
  print(f"""{Fore.LIGHTYELLOW_EX}
$$\                  $$$$$$\    $$\     
$$ |                $$  __$$\   $$ |    
$$ |       $$$$$$\  $$ /  \__|$$$$$$\   
$$ |      $$  __$$\ $$$$\     \_$$  _|  
$$ |      $$$$$$$$ |$$  _|      $$ |    
$$ |      $$   ____|$$ |        $$ |$$\ 
$$$$$$$$\ \$$$$$$$\ $$ |        \$$$$  |
\________| \_______|\__|         \____/ 
""")
  print(f"""{Fore.GREEN}logado em : {client.user}
ID do usuário : {client.user.id} """)
  print(f'{Fore.GREEN}dev : Left#0007')
  print(f'{Fore.GREEN}-=-' * 10)
  print('\n')
  await asyncio.sleep(2)
  if not os.path.exists(f'{client.user.id}.json'):
      with open(f'{client.user.id}.json', 'w') as f:
          json.dump({"emotef": False,"emotep": None, "statusf": False,"status": [], "servidor": None, "call": None}, f)
  with open(f'{client.user.id}.json', 'r') as f:
    data = json.load(f)
  await asyncio.sleep(3)
  if data['emotef'] == True:
    presence1 = True
  if data['statusf'] == True:
    statuschanger = True
    tasks.append(asyncio.create_task(statuszk()))
  if data['servidor'] and data['call']:
    calldetector = True
    tasks.append(asyncio.create_task(call_func()))
  try:
    if statuschanger == True:
      pass
    else:
      custom_status = {"custom_status": {"text": 'wannacry'}}
      r = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=geek(os.getenv("TOKEN")), json=custom_status)
      if r.status_code != 200:
        print(r.text)
  except Exception as error:
    print(f'{Fore.RED} | erro | {error} ')
  await asyncio.gather(*tasks)

async def ante_queda():
    async with aiohttp.ClientSession(headers=geek(my_secret6)) as session:
        while True:
          try:
            async with session.get('https://discord.com/api/v9/users/@me/') as response:
              print(f'{Fore.GREEN}Ante Queda Live : {response.status}')
              if 'Access denied | discord.com used Cloudflare to restrict access' in await response.text():
                  print('Cloudflare Ban Bypass !')
                  subprocess.run("kill 1", shell=True)
              elif 'You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently' in await response.text():
                  print('Cloudflare Ban Bypass !')
                  subprocess.run("kill 1", shell=True)
              elif "too many 4xx response codes" in await response.text():
                  print('Many requests solver')
                  subprocess.run("kill 1", shell=True)
          except Exception as error:
              print(f'{Fore.RED}[-][Ante queda ERRO] | {error}')
          await asyncio.sleep(120)

@client.command()
async def members(ctx, role: discord.Role):
    online_members = [member for member in ctx.guild.members if member.status != discord.Status.offline and role in member.roles]
    message = f"todos os membros no cargo {role}:\n"
    for member in online_members:
        message += f"{member.mention}\n"
    await ctx.send(message)
  
async def call_func():
  global calldetector
  while(True):
    if calldetector == True:
      try:
        with open(f'{client.user.id}.json', 'r') as f:
          data = json.load(f)
        if data['servidor'] and ['call']:
          servidor = data['servidor']
          call = data['call']
          try:
            guild = client.get_guild(servidor)
            voice = guild.voice_channels
          except Exception as error:
            print(f'{Fore.RED}[-][CALL FUNC ERROR] {error}')
            return
          await asyncio.sleep(1)
          conta = 0
          ids = []
          for VoiceChannel in voice:
            channel = client.get_channel(VoiceChannel.id)
            members = channel.members
            for Member in members:
              conta += 1
              ids.append(Member.id)
          if client.user.id not in ids:
            vc = discord.utils.get(client.get_guild(servidor).channels, id =call)
            await vc.guild.change_voice_state(channel=vc, self_mute=False, self_deaf=False)
          else:
            pass
          await asyncio.sleep(30)
        else:
          return
      except Exception as error:
        print('| ERROR :', error)
        return
    else:
      return

@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send('```ansi\n[2;34mComando não encontrado.[0m```', delete_after=3)
    return

@client.command(aliases=['cfarm'])
async def calldetector(ctx, servidor=None, call=None):
  await ctx.message.delete()
  global calldetector
  with open(f'{client.user.id}.json', 'r') as f:
    datacheck = json.load(f)
  if servidor == None and call == None:
    if datacheck['servidor'] and datacheck['call']:
      calldetector = True
      await ctx.send('```ansi\n[2;34mo calldetector foi re-ativado ! [0m```', delete_after=3)
      await call_func()
      return
    else:
      await ctx.send('```ansi\n[2;34mo seu calldetector não está configurado, use $calldetector {servidor-id} {call-id} ![0m```', delete_after=3)
      return
  else:
    pass
  if servidor == 'off' and calldetector == True:
    calldetector = False
    await ctx.send('```ansi\n[2;34mo calldetector foi desativado.[0m```', delete_after=3)
    return
  elif servidor == 'off' and calldetector == False:
    await ctx.send('```ansi\n[2;34mo calldetector não esta ativa.[0m```', delete_after=3)
    return
  elif servidor != None and call != None:
    try:
      ss = int(servidor)
      cc = int(call)
      calldetector = True
      await ctx.send('```ansi\n[2;34mcalldetector foi cofigurado e ativado, use $calldetector off para desativar e $calldetector para ativar ![0m```', delete_after=3)
    except:
      await ctx.send('```ansi\n[2;34menvie da seguinte forma, $calldetector {servidor-id} {call-id}[0m```', delete_after=3)
      return
  with open(f'{client.user.id}.json', 'r') as f:
    data = json.load(f)
  data['servidor'] = ss
  data['call'] = cc
  with open(f'{client.user.id}.json', 'w') as f:
    json.dump(data, f, indent=4)
  await call_func()

@client.command(aliases=['ping'])
async def never(ctx):
  await ctx.message.delete()
  latency = client.latency
  latencystr = str(f'{latency}')
  await ctx.send(f"""```ansi
[2;34mDeveloped by : Left
Contact : Https://e-z.bio/left

bot Latency : {latencystr[0:4]}ms[0m```""", delete_after=5)

@client.command(aliases=['av'])
async def avatar(ctx, *,member: discord.Member=None):
  await ctx.message.delete()
  if member == None:
    try:
      member = ctx.author
      userAvatarUrl = member.avatar
      await ctx.send(f"""```ansi\n[2;34mseu avatar : {member}[0m```""")
      await ctx.send(f"{userAvatarUrl}")
    except:
      await ctx.send('```ansi\n[2;34mmembro não encontrado no cache do bot.[0m```')
  else:
    userAvatarUrl = member.avatar
    await ctx.send(f"""```ansi\n[2;34mavatar de : {member}[0m```""")
    await ctx.send(f"{userAvatarUrl}")

@client.command(aliases=['bn'])
async def banner(ctx, *,member: discord.Member=None):
  await ctx.message.delete()
  if member == None:
    member = ctx.author
    req = await client.http.request(discord.http.Route("GET", f"/users/{member.id}"))
    banner_id = req["banner"]
    banner_collor = req["banner_color"]
    if banner_id:
      try:
        re2 = requests.get(f'https://cdn.discordapp.com/banners/{member.id}/{banner_id}.gif?size=1024')
        if re2.status_code == 200:
          banner_url = f'https://cdn.discordapp.com/banners/{member.id}/{banner_id}.gif?size=1024'
        else:
          banner_url = f"https://cdn.discordapp.com/banners/{member.id}/{banner_id}?size=1024"
      except Exception as error:
        print(f'{Fore.RED}[banner error] | {error}')
        return
      await ctx.send(f"```ansi\n[2;34mseu banner[0m```")
      await ctx.send(f"{banner_url}")
    else:
      banner_url = f"```ansi\n[2;34mvocê não tem banner, mas a cor que você usa é {banner_collor}.[0m```"
      await ctx.send(f"{banner_url}")
      return
  else:
    req = await client.http.request(discord.http.Route("GET", f"/users/{member.id}"))
    banner_id = req["banner"]
    banner_collor = req["banner_color"]
    if banner_id:
      try:
        re2 = requests.get(f'https://cdn.discordapp.com/banners/{member.id}/{banner_id}.gif?size=1024')
        if re2.status_code == 200:
          banner_url = f'https://cdn.discordapp.com/banners/{member.id}/{banner_id}.gif?size=1024'
        else:
          banner_url = f"https://cdn.discordapp.com/banners/{member.id}/{banner_id}?size=1024"
      except Exception as error:
        print(f'{Fore.RED}[banner error] | {error}')
        return
      await ctx.send(f"```ansi\n[2;34mbanner de {member.name}[0m```")
      await ctx.send(f"{banner_url}")
    else:
      banner_url = f"```ansi\n[2;34mo usuário não tem banner, mas a cor que ele usa é {banner_collor}.[0m```"
      await ctx.send(banner_url)
      
@client.command(aliases=["calljoiner","joinvoice"])
async def call(ctx, amount: int=None, amount1: int=None):
  await ctx.message.delete()
  if amount == None and amount1 == None:
    await ctx.send('```ansi\n[2;34menvie o comando no seguinte formato $call sv-id call-id[0m```', delete_after=7)
  else:
    vc = discord.utils.get(client.get_guild(amount).channels, id =amount1)
    await vc.guild.change_voice_state(channel=vc, self_mute=True, self_deaf=False)
    await ctx.send(f"""```ansi
[2;34mDeveloped by : Left 
Conectado com sucesso em :[0m``` <#{amount1}>""", delete_after=5)
    
@client.command(aliases=["ajuda","comandos"])
async def help(ctx):
   await ctx.message.delete()
   await ctx.send("""
```ansi
[2;34mDeveloped by: Left#0002
Server : .gg/wannacry
versão: beta 1.8.7

Status:
$off : status em Offline.
$dnd : status em Não Perturbe.
$idle : status em AFK.
$stop : parar atividades.

consulta:
$ip [ip] : consulta de endereço IP.
$cep [cep] : consulta de CEP.
$tel [numero] : puxa os dados registrados no número, cpf, nome, cidade etc.  [desativado]
$cpf [cpf] : puxa os dados do CPF. [desativado]
$av [ping/id] : puxa o avatar da pessoa marcada.
$bn [ping/id] : puxa o banner da pessoa marcada.

clear:
$ufriend : remove todos os amigos.
$allclear : apaga todas as dms e sai de todos os grupos.
$gclear : sai de todos os grupos.
$cclear : apaga todos os chats.
$leaver : sai de todos os servidores.
$purge [valor][off] : Apagar mensagens.

exploit:
$hiden [link mensagem] : deixa o final da mensagem invisível, sendo possível esconder links.
$invert [mensagem] : inverte o lugar que aparece "editado".

troll:
$infinite [off] : fica aparecendo o tempo todo que você está digitando.
$trava : envia um texto 10 vezes para lagar o canal.

profile:
$stream [nome] : Status em Streaming.
$changer [off][nickname] : nickname animado no servidor.
$switch [off] : muda a presença de on para dnd para afk em loop.
$status [off][help][status] : status animado/fixo.
$house [help] : muda o seu hypesquad, opções 1 - 3.
$hchanger [off] : deixa a sua conta com 2 hypesquad.

always on:
$cfarm [servidor.id call.id] : sistema de detecção para manter 24/7 na mesma call.
$emoji [help][emote.id or emote] : adiciona uma reação sempre que você for marcado.

utils:
$ping : retorna o ping/latency do bot.
$afk [seu texto] : envia um texto enquanto você está afk. 
$reset : força o bot a reiniciar com um novo ip.
$ceo : bio do criador.
$help : lista de comandos.
$suporte : servidor de suporte.[0m
```
""", delete_after=18)

@client.command()
async def off(ctx):
  await ctx.message.delete()
  await client.change_presence(activity=None, status=discord.Status.offline)
  await ctx.send('```ansi\n[2;34mStatus alterado para offline com sucesso ![0m```', delete_after=5)
  
@client.command()
async def stop(ctx):
  await ctx.message.delete()
  await client.change_presence(activity=None, status=discord.Status.dnd)
  await ctx.send('```ansi\n[2;34matividades paradas com sucesso ![0m```', delete_after=5)
  
@client.command()
async def dnd(ctx):
  await ctx.message.delete()
  await client.change_presence(activity=None, status=discord.Status.do_not_disturb)
  await ctx.send('```ansi\n[2;34mStatus alterado para Do_not_disturb com sucesso ![0m```', delete_after=5)
  
@client.command()
async def idle(ctx):
  await ctx.message.delete()
  await client.change_presence(activity=None, status=discord.Status.idle)
  await ctx.send('```ansi\n[2;34mStatus alterado para idle com sucesso ![0m```', delete_after=5)

@client.command(aliases=['suporte'])
async def servidor(ctx):
  await ctx.message.delete()
  await ctx.send('discord.gg/zemUqjReEE')

@client.command()
async def switch(ctx, amount=None):
  global statuschanger
  if statuschanger == True:
    await ctx.send('```ansi\n[2;34mDesative o status animado para usar o switch ⚠[0m```', delete_after=5)
    return
  else:
    await ctx.message.delete()
    global switch1
    if amount == None and switch1 == False:
      switch1 = True
      await ctx.send('```ansi\n[2;34mo switch foi ativado ![0m```', delete_after=4)
      while True:
        if switch1 == False:
          return
        else:
          await client.change_presence(status=discord.Status.online)
          await asyncio.sleep(1)
          await client.change_presence(status=discord.Status.idle)
          await asyncio.sleep(1)
          await client.change_presence(status=discord.Status.do_not_disturb)
          await asyncio.sleep(1.5)
    elif amount == None and switch1 == True:
      await ctx.send('```ansi\n[2;34mo switch já está ativado, use $switch off para desativar ![0m```', delete_after=4)
      return
    elif amount == 'off':
      switch1 = False
      await ctx.send('```ansi\n[2;34mo switch foi desativado ![0m```', delete_after=4)
      return
  
@client.command(aliases=["stream"])
async def status_stream(ctx, *sexy):
  global statuschanger
  amount = " ".join(sexy)
  await ctx.message.delete()
  if amount == 'help':
    await ctx.send('```ansi\n[2;34ma função streaming pode ter alguns problemas tipo :\n\no streaming não ser ativado, caso isso ocorra você pode tentar por algo diferente no streaming tipo $streaming ola mundo!\n\nlembrando que é necessário esperar alguns minutos após desligar o status.[0m```')
    return
  if statuschanger == True:
    await ctx.send('```ansi\n[2;34mdesative o status e espere 1 minuto, após isso use o streaming de novo, caso não funcione coloque um nome diferente.[0m```', delete_after=6)
    return
  else:
    if amount == None:
      amount = '.gg/zemUqjReEE'
    streaming = discord.Streaming(name=f"{amount}", url="https://www.youtube.com/watch?v=NgsWGfUlwJI")
    await client.change_presence(status=discord.Status.do_not_disturb, activity=streaming)
    await ctx.send('```ansi\n[2;34mStatus alterado para streaming com sucesso ![0m```', delete_after=5)
    await asyncio.sleep(1)

@client.command(aliases=["ceo"])
async def self(ctx):
  await ctx.message.delete()
  await ctx.send('https://e-z.bio/left')
  
@client.command(aliases=["purge","excluir","cl"])
async def apagar(ctx, amount=None):
  global purge0, purge1
  await ctx.message.delete()
  if amount == 'off' and purge0 == True:
    await ctx.send('```ansi\n[2;34mo Purge foi cancelado![0m```', delete_after=3)
    purge0 = False
    purge1 = False
    return
  elif amount == 'off' and purge0 == False:
    await ctx.send('```ansi\n[2;34mo Purge não está ativado.[0m```', delete_after=3)
    return
  try:
    amount = int(amount)
    purge0 = True
  except ValueError:
    await ctx.send("```ansi\n[2;34musa o comando direito seu newba, $purge { quantidade }[0m```", delete_after=3)
  if amount < 9999 and purge1 == True:
    await ctx.send('```ansi\n[2;34mo Purge já está ativado, cancele ou aguarde o termino da tarefa.[0m```', delete_after=3)
    return
  await asyncio.sleep(0.7)
  papagar = amount
  apagadas = 0
  if int(amount) < 36:
    purge1 = True
    async for message in ctx.channel.history(limit=9999):
      if message.type == discord.MessageType.call:
          continue
      if message.author.id == client.user.id and apagadas != papagar:
          try:
            if apagadas == papagar:
              return
            if purge0 == False:
              return
            else:
              await message.delete()
              apagadas += 1
          except:
            pass
      else:
        pass
    purge1 = False
  elif int(amount) > 36:
    purge1 = True
    async for message in ctx.channel.history(limit=9999):
      if message.type == discord.MessageType.call:
          continue
      if message.author.id == client.user.id and apagadas != papagar:
          try:
            if apagadas == papagar:
              return
            if purge0 == False:
              return
            else:
              await message.delete()
              apagadas += 1
            await asyncio.sleep(2.4)
          except:
            pass
      else:
        pass
    purge1 = False
  elif int(amount) > 2001:
    await ctx.send('```ansi\n[2;34mo limite do purge é 2000 por vez.[0m```', delete_after=5)
    return

@client.command(aliases=['emoji'])
async def presence(ctx, amount=None):
  global presence1
  await ctx.message.delete()
  with open(f'{client.user.id}.json', 'r') as f:
    data = json.load(f)
  if amount == 'off':
    presence1 = False
    data['emotef'] = False
    with open(f'{client.user.id}.json', 'w') as f:
      json.dump(data, f, indent=4)
    await ctx.send('```ansi\n[2;34mA função emote foi desativada.[0m```', delete_after=5)
    return
  elif amount == 'help':
    await ctx.send('```ansi\n[2;34mcaso você queira adicionar um emote comum ( emote sem nitro ) use $emote 😃 e o seu emote. \ncaso você queira adicionar um emote de nitro é necessário pegar o id. \n\emote coloque o emote ao lado da barra, assim irá aparecer algo tipo "<a:Gcheck:752281845885829231>" assim você pega o id e usa $emote 752281845885829231, simples.[0m```')
    return
  id2 = data['emotep']
  if amount is None and id2 != None and presence1 == False:
    data['emotef'] = True
    with open(f'{client.user.id}.json', 'w') as f:
      json.dump(data, f, indent=4)
    presence1 = True
    await ctx.send("```ansi\n[2;34mo presence foi ativado ![0m```", delete_after=5)
    return
  elif amount is None and id2 != None and presence1 == True:
    await ctx.send("```ansi\n[2;34mo emote já está ativado, use $emote off para desativar.[0m```", delete_after=4)
    return
  elif amount is None and id2 == None:
    await ctx.send("```ansi\n[2;34mmanda o id de um emote seu newba, \emote só colocar o emote ao lado da barra.[0m```", delete_after=5)
    return
  if isinstance(amount, str):
    emoji_pattern = re.compile("[^\u0000-\u00FF]+")
    if emoji_pattern.match(amount):
      with open(f'{client.user.id}.json', 'r') as f:
        data = json.load(f)
      data['emotep'] = amount
      with open(f'{client.user.id}.json', 'w') as f:
        json.dump(data, f, indent=4)
      await ctx.send('```ansi\n[2;34memote adicionado com sucesso, lembre-se de ativar a função.[0m```', delete_after=7)  
    else:
      try:
        amount = int(amount)
        emoji = client.get_emoji(amount)
        with open(f'{client.user.id}.json', 'r') as f:
          data = json.load(f)
        data['emotep'] = amount
        with open(f'{client.user.id}.json', 'w') as f:
          json.dump(data, f, indent=4)
        await ctx.send('```ansi\n[2;34memote adicionado com sucesso, lembre-se de ativar a função.[0m```', delete_after=10)  
      except Exception as error:
        print(error)
        await ctx.send("```ansi\n[2;34messe não é um id válido ou emote válido, use $presence help em caso de dúvidas..[0m```", delete_after=10)
  else:
    try:
      amount = int(amount)
      emoji = client.get_emoji(amount)
      with open(f'{client.user.id}.json', 'r') as f:
        data = json.load(f)
      data['emotep'] = amount
      with open(f'{client.user.id}.json', 'w') as f:
        json.dump(data, f, indent=4)
      await ctx.send('```ansi\n[2;34memote adicionado ![0m```', delete_after=5)
    except Exception as error:
      print(error)
      await ctx.send("```ansi\n[2;34messe não é um id válido ou emote válido, use $presence help em caso de dúvidas.[0m```", delete_after=5) 

@client.event  
async def on_message(message):
  global emojis1, presence1, notperm
  if message.channel.id in notperm:
    await client.process_commands(message)
    return
  if str(client.user.id) in message.content and presence1 == True:
    if message.type == discord.MessageType.call:
      return
    if str(client.user.id) in message.content and client.user in message.mentions:
      if message.author.id == emojis1:
        return
      try:
        if presence1 == False:
          return
        with open(f'{client.user.id}.json', 'r') as f:
          data = json.load(f)
        emojis1 = message.author.id
        try:
          emoji = int(data['emotep'])
          emoji = client.get_emoji(data['emotep'])
        except:
          emoji = data['emotep']
        await message.add_reaction(emoji)
      except Exception as errorkb:
        if "Missing Permissions" in str(errorkb):
          notperm.append(message.channel.id)
          print(f"| ERROR Presence: kbmissing {message.channel.id}", errorkb)
        pass
  await client.process_commands(message)

async def afkzk():
  @client.event
  async def on_message(message):
    global grupos, respondidos, afkb2, afkb4, afkold
    reply = '```afk ativado, envie uma mensagem em qualquer lugar para desativar.```'
    if message.author == client.user and message.content != afkb4 and message.content != reply and afkb2 == True:
      respondidos.clear()
      afkb2 = False
      await client.change_presence(activity=None, status=discord.Status.do_not_disturb)
      await client.process_commands(message)
      return
    if not message.guild:
      if message.channel.id in grupos or message.channel.id in respondidos:
        await client.process_commands(message)
        return
      else:
        for channel in client.private_channels:
          if isinstance(channel, discord.GroupChannel):
            if channel.id not in grupos:
              grupos.append(channel.id)
        if afkb2 == False:
          await client.process_commands(message)
          return
        if message.author != client.user and message.content != afkb4 and not message.guild and afkb2 == True and message.content != reply:
          mensagg = str(afkb4)
          await message.channel.send(f'{mensagg}')
          respondidos.append(message.channel.id)
          await asyncio.sleep(0.5)
          payload = {'manual': True, 'mention_count': 1}
          req = requests.post(f'https://discordapp.com/api/channels/{message.channel.id}/messages/{message.id}/ack', headers=geek(my_secret6), json=payload)
    await client.process_commands(message)

@client.command()
async def afk(ctx, *sexo):
  global afkb2, afkb3, afkb4, respondidos
  await ctx.message.delete()
  mensagem = " ".join(sexo)
  if mensagem == '':
    await ctx.send('```ansi\n[2;34mescreve o motivo de você estar ficando afk seu newba.[0m```', delete_after=6)
  else:
    await client.change_presence(status=discord.Status.idle)
    if afkb3 == False:
      afkb4 = str(f'```ansi\n[2;34m[AFK] wannacry [AFK]\n\n{mensagem}[0m```')
      afkb2 = True
      afkb3 = True
      await ctx.send("```ansi\n[2;34mafk ativado, envie uma mensagem em qualquer lugar para desativar.[0m```", delete_after=9)
      await afkzk()
    elif afkb3 == True:
      await ctx.send("```ansi\n[2;34mafk ativado, envie uma mensagem em qualquer lugar para desativar.[0m```", delete_after=9)
      respondidos.clear()
      afkb4 = str(f'```ansi\n[2;34m[AFK] wannacry [AFK]\n\n{mensagem}[0m```')
      afkb2 = True

@client.command()
async def ip(ctx, amount=None):
  await ctx.message.delete()
  if amount == None:
    await ctx.send("```ansi\n[2;34mcoloque o IP após o comando ![0m```", delete_after=8)
    return
  else:
    try:
      req = requests.get(f"https://ipinfo.io/{amount}/json")
      data = req.json()
      ip = data.get('ip')
      hostname = data.get('hostname')
      city = data.get('city')
      country = data.get('country')
      region = data.get('region')
      org = data.get('org')
      loc = data.get('loc')
      await ctx.send(f"""```ansi
[2;34mDeveloped by : Left
Contact : Https://e-z.bio/left

ip : {ip}
hostname : {hostname}
city : {city}
country : {country}
region : {region}
org : {org}
loc : {loc}[0m```""", delete_after=20)
    except:
      await ctx.send('```ansi\n[2;34merro, escreva no formato certo, exemplo 123123-123 |[0m```')

@client.command()
async def cep(ctx, amount=None):
  await ctx.message.delete()
  if amount == None:
    await ctx.send("```ansi\n[2;34m| envie no formato 06233-030 |[0m``` ", delete_after=5)
  else:
    try:
      req = requests.get(f"https://cdn.apicep.com/file/apicep/{amount}.json")
      data = req.json()
      cep = data.get("code")
      estado = data.get("state")
      cidade = data.get("city")
      distrito = data.get("district")
      endereco = data.get("address")
      await ctx.send(f"""```ansi
[2;34mDeveloped by : Left
Contact : Https://e-z.bio/left
Cep : {cep}
estado : {estado}
cidade : {cidade}
distrito : {distrito}
endereço : {endereco}  
[0m```""", delete_after=20)
    except Exception as error:
      print(f"{Fore.RED}[-] {error}")
      await ctx.send("```ansi\n[2;34merro, escreva no formato certo, exemplo 123123-123 |[0m```", delete_after=8)
      pass
  
@client.command(aliases=['flood','spamming'])
async def spam(ctx, amount:int=None, *sexy):
  message = " ".join(sexy)
  await ctx.message.delete()
  valor = amount
  while valor != 0:
    await ctx.send(f'{message}')
    valor -= 1 

async def statuszk():
  global statuschanger
  statusold = None
  while True:
    if statuschanger == True:
      with open(f'{client.user.id}.json', 'r') as f:
        data = json.load(f)
      status_list = data['status']
      if status_list == []:
        statuschanger = False
        return
      for statusmk in status_list:
        if statusold == str(statusmk):
          await asyncio.sleep(6)
          continue
        try:
          if statuschanger == True:
            custom_status = {"custom_status": {"text": f'{statusmk}'}}
            async with aiohttp.ClientSession(headers=geek(my_secret6)) as session:
              async with session.patch("https://discord.com/api/v9/users/@me/settings", json=custom_status) as r:
                if r.status == 200:
                  statusold = str(statusmk)
                elif "too many 4xx response codes" in await r.text():
                  print('Many requests solver')
                  await asyncio.sleep(5)
                else:
                  print(f'{Fore.RED}[-][STATUS ERROR][{r.status}] | {await r.text()}')
                await asyncio.sleep(5)
          else:
              return
        except Exception as error:
            print(f'{Fore.RED}[-][STATUS ERROR] | {error}')
            subprocess.run("kill 1", shell=True)
    else:
      return
    
@client.command()
async def status(ctx, *sexy: str):
  await ctx.message.delete()
  global statuschanger
  amount = sexy
  if all(not s for s in amount):
    amount = None
  if amount == None and statuschanger == True:
    await ctx.send('```ansi\n[2;34ma função já está ativada, use $status off para desativar.[0m```', delete_after=4)
    return
  elif amount == None and statuschanger == False and switch1 == True:
    await ctx.send('```ansi\n[2;34mdesative o switch para usar o status animado.[0m```', delete_after=4)
    return
  try:
    if amount == None:
      statuschanger = True
      print (statuschanger)
    else:
      amount = " ".join(sexy)
      if amount == 'off':
        with open(f'{client.user.id}.json', 'r') as f:
          data = json.load(f)
        data['statusf'] = False
        with open(f'{client.user.id}.json', 'w') as f:
          json.dump(data, f, indent=4)
        await ctx.send('```ansi\n[2;34mstatus animado foi desativado![0m```', delete_after=3)
        statuschanger = False
        return
      elif amount == 'list':
        with open(f'{client.user.id}.json', 'r') as f:
          data = json.load(f)
        datas = data['status']
        await ctx.send(f'```ansi\n[2;34mvocê tem esses itens no status :\n{datas}[0m```', delete_after=10)
        return
      elif amount == 'help':
        await ctx.send('```ansi\n[2;34mcomo usar :\nuse $status list para retornar todos os status que você tem\nuse $status off para desativar a função\nuse $status {seu status} para adicionar um novo\nuse $status {nome exato do status} para remover um status![0m```', delete_after=10)
        return
      else:
        pass
  except Exception as error:
    print(f'{Fore.red}[-][STATUS ERROR] | {error}')
  if amount == None:
    with open(f'{client.user.id}.json', 'r') as f:
      data = json.load(f)
      statusl = data["status"]
      if statusl == []:
        await ctx.send('```ansi\n[2;34mvocê não tem status salvo, use $status {seu status} para adicionar algum![0m```', delete_after=10)
        statuschanger = False
        return
      else:
        with open(f'{client.user.id}.json', 'r') as f:
          data = json.load(f)
        data['statusf'] = True
        with open(f'{client.user.id}.json', 'w') as f:
          json.dump(data, f, indent=4)
        await ctx.send('```ansi\n[2;34mStatus Changer foi ativado com sucesso![0m```', delete_after=5)
        taskg = asyncio.create_task(statuszk())
  else:
    with open(f'{client.user.id}.json', 'r') as f:
        data = json.load(f)
    if amount in data['status']:
        data['status'].remove(amount)
        await ctx.send('```ansi\n[2;34mStatus removido com sucesso![0m```', delete_after=5)
    else:
        data['status'].append(amount)
        await ctx.send('```ansi\n[2;34mStatus adicionado com sucesso, lembre-se de ativar a função ![0m```', delete_after=5)
    with open(f'{client.user.id}.json', 'w') as f:
        json.dump(data, f, indent=4)

@client.command(aliases=['ufriend'])
async def unfriender(ctx):
  await ctx.message.delete()
  geter = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=geek(my_secret6)).json()
  certo = 0
  errado = 0
  if not geter:
    print (f"{Fore.RED}Nenhum amigo foi detectado.")
    await ctx.send("```ansi\n[2;34mvocê não tem amigos seu anti social.[0m```")
    return
  else:
    await ctx.send('```ansi\n[2;34mdeletando amigos![0m```', delete_after=5)
    for friend in geter:
      try:
        requests.delete('https://discord.com/api/v9/users/@me/relationships/'+friend['id'], headers=geek(my_secret6))
        certo += 1
      except Exception as error:
        print(f"{Fore.RED}[-] {error}")
        errado += 1
        return
    await ctx.send(f"""```ansi\n[2;34mapagados: {certo}\nerros : {errado} [0m```""", delete_after=6)

@client.command(aliases=['allclear'])
async def dmcleaner(ctx):
  await ctx.message.delete()
  await ctx.send("```ansi\n[2;34mlimpando ![0m```", delete_after=2)
  canal = requests.get("https://discord.com/api/v8/users/@me/channels", headers=geek(my_secret6)).json()
  if not canal:
    await ctx.send('```você não tá em nenhuma dm, vai conversar com alguém seu anti social.```', delete_after=5)
    return
  channelid = []
  for channel in canal:
    channelid.append(channel['id'])
  for chanel in channelid:
    try:
      f = requests.delete('https://discord.com/api/v8/channels/'+chanel, headers=geek(my_secret6))
      if f.status_code == 200:
          print(f'{Fore.GREEN}[+][apagado com sucesso] {f.status_code} | {f.text}')
      else:
          print(f'{Fore.RED}[-][erro : {f.status_code} | {f.text}]')
    except Exception as error:
        print(f"{Fore.RED}[-] {error}")

@client.command()
async def leaver(ctx):
  await ctx.send("```ansi\n[2;34msaindo dos servidores. . .[0m```", delete_after=3)
  servidores = requests.get("https://discord.com/api/v8/users/@me/guilds", headers=geek(my_secret6)).json()
  if not servidores:
    await ctx.send('```ansi\n[2;34mvocê não tem servidores na sua conta, larga de ser anti social e vai consersar.[0m```', delete_after=9)
    return
  for guild in servidores:
    try:
      requests.delete('https://discord.com/api/v8/users/@me/guilds/'+guild['id'], headers={'Authorization': my_secret6})
      print(f"{Fore.GREEN} server leaver : "+guild['name'])
    except Exception as error:
      print (f"{Fore.RED}[-] {error}")

@client.command()
async def infinite(ctx, amount=None):
  global infinite1
  await ctx.message.delete()
  if infinite1 == True and amount == None:
    await ctx.send('```ansi\n[2;34msó pode ser usado uma vez, use $infinite off para desativar.[0m```', delete_after=3)
    return
  if amount == None and infinite1 == False:
    await ctx.send('```ansi\n[2;34mo infinite foi ativado ![0m```', delete_after=3)
    infinite1 = True
  elif amount == 'off' and infinite1 == True:
    await ctx.send('```ansi\n[2;34mInfinite foi desligado com sucesso ![0m```', delete_after=2)
    infinite1 = False
  elif amount == 'off' and infinite1 == False:
    await ctx.send('```ansi\n[2;34mo infinite não está ativado[0m```', delete_after=2)
    return
  channel = ctx.message.channel.id
  if ctx.message.guild:
    await ctx.send('```ansi\n[2;34mo comando só pode ser utilizado em DM.[0m```', delete_after=3)
    return
  else:
    while True:
      try:
        if infinite1 == True:
          requests.post(f'https://discord.com/api/v9/channels/{channel}/typing', headers=geek(my_secret6))
          await asyncio.sleep(7)
          pass
        else:
          break
      except Exception as error:
        print(f'{Fore.RED} [-] error Infinite : {error}')
        break

@client.command()
async def hiden(ctx, hidden, *sexy):
  message = " ".join(sexy)
  await ctx.message.delete()
  await ctx.send(message + ('||\u200b||' * 200) + hidden)

@client.command()
async def invert(ctx, *sexy):
  message = " ".join(sexy)
  await ctx.message.delete()
  text = await ctx.send(message)
  await text.edit(content=f"\u202b{message}")

@client.command()
async def tel(ctx, numero):
  await ctx.message.delete()
  from bs4 import BeautifulSoup
  import requests
  try:
    numero2 = int(numero)
  except:
    await ctx.send('```ansi\n[2;34menvia um número válido seu newba, sem traços, espaço etc.[0m```', delete_after=4)
    return
  if numero == '1':
    return
  else:
    session = requests.Session()
    fuck = {'Tel': f'{numero}'}
    coki = {'tk': '1bb1cec3-b3d3-4bec-8a4f-d683c9518ea9'}
    try:
      page = session.get(f'https://i-find.org/consultar/Telefone/?Tel={numero}', data=fuck, cookies=coki)
      if page.status_code != 200:
        await ctx.send('```ansi\n[2;34mocorreu um problema na requisição da API, contate o Left#1303[0m```', delete_after=5)
        return
      elif page.status_code == 200:
        html = page.text
        try:
          soup = BeautifulSoup(html, 'html.parser')
          operadora = soup.select_one('th:contains("Operadora") + td')
          operadora = operadora.text if operadora else None
          cep1 = soup.select_one('th:contains("CEP") + td')
          cep1 = cep1.text if cep1 else None
          bairro = soup.select_one('th:contains("Bairro") + td')
          bairro = bairro.text if bairro else None
          numero = soup.select_one('th:contains("Complemento") + td')
          numero = numero.text if numero else None
          telefone = soup.select_one('th:contains("Telefone") + td')
          telefone = telefone.text if telefone else None
          cpf = soup.select_one('th:contains("CPF") + td')
          cpf = cpf.text if cpf else None
          nome = soup.select_one('th:contains("Nome") + td')
          nome = nome.text if nome else None
          endereco = soup.select_one('th:contains("Endereco") + td')
          endereco = endereco.text if endereco else None
        except Exception as error:
          print(error)
          await ctx.send('```ansi\n[2;34mocorreu um erro ao extrair as informações, contate o Left#1303[0m```', delete_after=5)
          return
        await ctx.send(f'```ansi\n[2;34mDeveloped by Left#1303\n\nTelefone {telefone}\nnome: {nome}\ncpf: {cpf}\nendereço: {endereco}\nnumero: {numero}\nbairro: {bairro}\ncep: {cep1}\noperadora: {operadora}[0m```', delete_after=10)
    except Exception as error:
      print (error)
      await ctx.send('```ansi\n[2;34mOcorreu um erro inesperado.[0m```')

  
@client.command(aliases=['nickanimado','nickchanger','animado'])
async def changer(ctx, amount=None):
  global changer1
  tx = ['$','&','/','\ ']
  if amount == None:
    await ctx.send('```ansi\n[2;34mAdicione um nome para ser usado na troca ( obs 7 letras )[0m```', delete_after=6)
    return
  if amount == 'off' and changer1 == True:
      await ctx.message.delete()
      changer1 = False
      await ctx.send('```ansi\n[2;34mo changer foi desativado ![0m```', delete_after=3)
      return
  elif amount == 'off' and changer1 == False:
      await ctx.message.delete()
      await ctx.send('```ansi\n[2;34mo changer não está ativado.[0m```', delete_after=3)
      return
  if ctx.channel.type is discord.ChannelType.private:
      await ctx.message.delete()
      await ctx.send('```ansi\n[2;34mO comando só pode ser utilizado em Servidores.[0m```', delete_after=5)
      return
  elif len(amount)>7:
      await ctx.message.delete()
      await ctx.send('```ansi\n[2;34mO nome não pode ter mais que 7 letras[0m```', delete_after=5)
      return
  else:
      await ctx.message.delete()
      await ctx.send('```ansi\n[2;34mNome animado foi ativado ![0m```', delete_after=5)
      changer1 = True
  while True:
      member = ctx.author
      nomes = amount
      for i, letter in enumerate(nomes):
          if changer1 == False:
              return
          elif i == len(nomes) - 1:
              await member.edit(nick=nomes)
          else:
              await member.edit(nick=nomes[:i+1] + tx[i%len(tx)])
              await asyncio.sleep(0.5)
      await asyncio.sleep(300)

@client.command(aliases=['reset'])
async def reboot(ctx):
  await ctx.message.delete()
  await ctx.send('```ansi\n[2;34mo bot irá reiniciar, aguarde 1 - 5 minutos.[0m```')
  try:
    subprocess.run("kill 1", shell=True)
  except:
    await ctx.send('```ansi\n[2;34mOcorreu um erro ao tentar reiniciar, tente novamente mais tarde.[0m```', delete_after=3)

@client.command(aliases=['house'])
async def hypechanger(ctx, amount=None):
  await ctx.message.delete()
  if amount == 'help':
    await ctx.send('```ansi\n[2;34mas opções são:\n1 : Hype Squad Bravery\n2 : Hype Squad Brilliance\n3 : Hype Squad Balance\nuse $hypechanger (sua opção)[0m```', delete_after=6)
    return
  else:
    try:
      hype = int(amount)
      if hype > 4:
        await ctx.send('```ansi\n[2;34mas opções vão apenas de 1 a 3.[0m```', delete_after=4)
        return
    except:
      await ctx.send('```ansi\n[2;34menvie da seguinte forma: $hypechanger {valor de 1 a 3}[0m```', delete_after=4)
      return
    hypesqad_req = {'house_id': f'{hype}'}
    v = requests.post('https://discord.com/api/v9/hypesquad/online', headers=geek(my_secret6), json=hypesqad_req)
    if v.status_code == 200 or 204:
      await ctx.send('```ansi\n[2;34mo seu hypesquad foi alterado com sucesso![0m```', delete_after=4)
    else:
      await ctx.send('```ansi\n[2;34mocorreu um problema na tentativa de alterar o hypesquad, contate o Left#0007.[0m```', delete_after=4)

@client.command()
async def trava(ctx):
  for i in range(0, 10):
    ascii = ""
    for x in range(1985):
      num = random.randrange(13000)
      ascii = ascii + chr(num)
    await ctx.send(f'{ascii}')

@client.command(aliases=['hchanger'])
async def anihype(ctx, amount=None):
  global anihype1
  await ctx.message.delete()
  if anihype1 == True and amount is None:
    await ctx.send('```ansi\n[2;34mo hchanger já está ativado, use $hchanger off para desativar.[0m```', delete_after=4)
  elif anihype1 == True and amount == 'off':
    anihype1 = False
    await ctx.send('```ansi\n[2;34mo hchanger foi desativado.[0m```', delete_after=4)
    return
  elif anihype1 == False and amount is None:
    await ctx.send('```ansi\n[2;34mo hchanger vai ser ativado.[0m```', delete_after=4)
    anihype1 = True
    while True:
      hypereq = ['1','2','3']
      for hype in hypereq:
        if anihype1 == False:
          return
        else:
          hypesqad = {'house_id': f'{hype}'}
          v = requests.post('https://discord.com/api/v9/hypesquad/online', headers=geek(my_secret6), json=hypesqad)
          if v.status_code == 204:
            await asyncio.sleep(17)
          else:
            print(f"{Fore.RED}[-][aninhype error] {v.status_code} | {v.text}")
            await asyncio.sleep(20)

@client.command()
async def cclear(ctx):
    gps = []
    for channel in client.private_channels:
        if isinstance(channel, discord.GroupChannel):
            gps.append(channel.id)
    delete = []
    await ctx.message.delete()
    await ctx.send('```ansi\n[2;34mcomeçando a apagar.[0m```', delete_after=10)
    dms = []
    for channel in client.private_channels:
      if isinstance(channel, discord.DMChannel) and isinstance(channel.recipient, discord.User):
        dms.append(channel.id)
    for canal in dms:
      try:
        f = requests.delete('https://discord.com/api/v8/channels/'+str(canal), headers=geek(my_secret6))
        if f.status_code == 200:
          pass
        else:
          print(f'{Fore.RED}[-][erro : {f.status_code} | {f.text}]')
      except Exception as error:
          print(f"{Fore.RED}[-] {error}")

@client.command()
async def gclear(ctx):
  gps = []
  for channel in client.private_channels:
    if isinstance(channel, discord.GroupChannel):
      gps.append(channel.id)
  await ctx.send('```ansi\n[2;34mcomeçando a apagar.[0m```', delete_after=10)
  for canal in gps:
    try:
      f = requests.delete('https://discord.com/api/v8/channels/'+str(canal), headers=geek(my_secret6))
      if f.status_code == 200:
        pass
      else:
        print(f'{Fore.RED}[-][erro : {f.status_code} | {f.text}]')
    except Exception as error:
        print(f"{Fore.RED}[-] {error}")

async def runner():
    while True:
      try:
        await client.start(my_secret6)
      except:
        session = requests.Session()
        response = session.get('https://discord.com/api/v9/users/@me/')
        if 'Access denied | discord.com used Cloudflare to restrict access' in response.text:
          print('Cloudflare Ban Bypass !')
          subprocess.run("kill 1", shell=True)
        elif 'You are being blocked from accessing our API temporarily due to exceeding our rate limits frequently' in response.text:
          print('Cloudflare Ban Bypass !')
          subprocess.run("kill 1", shell=True)
        elif 'Not found' in response.text:
          print(f'{Fore.RED}Token Inválida.')
        else:
          print(response.status_code, response.text)  
          return
      await asyncio.sleep(5)

async def live():
  while True:
    await asyncio.sleep(5)
    a = 1

if __name__ == '__main__':
    keep_alive_thread = threading.Thread(target=keep_alive)
    keep_alive_thread.start()
    asyncio_thread = threading.Thread(target=asyncio.run, args=(runner(),))
    asyncio_thread.start()
    asyncio.run(live())
