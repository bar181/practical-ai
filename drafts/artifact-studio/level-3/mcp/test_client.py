"""test_client.py [--write]

Starts server.py over stdio, calls every tool through a real MCP client and prints what came back.
With --write it also files one test note in base/inspiration/inbox/. Delete that note afterwards.
"""
import asyncio, sys, json, os
from mcp import ClientSession, StdioServerParameters, stdio_client
S=os.path.join(os.path.dirname(os.path.abspath(__file__)),'server.py')
def val(r):
    sc=getattr(r,'structured_content',None)
    if sc is not None: return sc.get('result',sc) if isinstance(sc,dict) and set(sc)=={'result'} else sc
    texts=[getattr(c,'text','') for c in r.content]
    try: out=[json.loads(t) for t in texts]
    except ValueError: return texts[0] if len(texts)==1 else texts
    return out[0] if len(out)==1 else out
async def main():
    async with stdio_client(StdioServerParameters(command=sys.executable,args=[S])) as (r,w):
        async with ClientSession(r,w) as s:
            init=await s.initialize(); print('server:',init.server_info.name if hasattr(init,'server_info') else init.serverInfo.name)
            tools=(await s.list_tools()).tools; print('tools:',[t.name for t in tools])
            o=val(await s.call_tool('studio_overview',{})); print('overview counts:',o['counts'])
            rec=val(await s.call_tool('recommend',{'goal':'sell','audience':'customer','format':'any'})); print('recommend:',[(x['format'],x['title']) for x in rec])
            t=val(await s.call_tool('get_template',{'id':'deck-visionary','part':'source'})); print('template source chars:',len(t['source']))
            for tid in ('deck-story','social-carousel','recipe-report'):
                t=val(await s.call_tool('get_template',{'id':tid,'part':'starter'})); print('starter for',tid,{k:len(v) for k,v in t['files'].items()})
            x=await s.call_tool('get_template',{'id':'deck-story','part':'everything'}); print('wrong part ->',x.content[0].text[:80])
            c=val(await s.call_tool('get_component',{'id':'svg-line-draw'})); print('svg code starts:',c['code'][:40])
            c2=val(await s.call_tool('get_component',{'id':val(await s.call_tool('list_components',{'group':'page'}))[0]['id']})); print('page part code chars:',len(c2.get('code','')),c2['name'])
            rules=val(await s.call_tool('get_rules',{'which':'checklist'})); print('checklist chars:',len(rules if isinstance(rules,str) else rules[0]))
            bad=await s.call_tool('recommend',{'goal':'nope','audience':'customer'}); print('bad input is an error:',getattr(bad,'is_error',getattr(bad,'isError',None)),str(val(bad))[:110])
            if '--write' in sys.argv:
                a=val(await s.call_tool('add_inspiration',{'title':'Test note','what_works':'A test.','tags':'test'})); print('saved:',a['saved'])
asyncio.run(main())
