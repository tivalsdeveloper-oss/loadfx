"""Terminal widgets for loadfx 2.0."""
import os, shutil, sys

class Table:
    def __init__(self, headers, rows=(), style="grid", padding=1, stream=None):
        self.headers=[str(x) for x in headers]; self.rows=[list(map(str,r)) for r in rows]
        self.style=style; self.padding=max(0,int(padding)); self.stream=stream or sys.stdout
    def add_row(self,row):
        if len(row)!=len(self.headers): raise ValueError("row length must match headers")
        self.rows.append(list(map(str,row))); return self
    def render(self):
        widths=[max([len(self.headers[i])]+[len(r[i]) for r in self.rows]) for i in range(len(self.headers))]
        p=" "*self.padding
        if self.style=="rounded": tl,tr,bl,br,h,v,join="╭","╮","╰","╯","─","│","┼"
        elif self.style=="double": tl,tr,bl,br,h,v,join="╔","╗","╚","╝","═","║","╬"
        elif self.style=="minimal":
            def row(vals): return "  ".join(f"{v:<{w}}" for v,w in zip(vals,widths))
            return "\n".join([row(self.headers),row(["-"*w for w in widths])]+[row(r) for r in self.rows])
        else: tl,tr,bl,br,h,v,join="+","+","+","+","-","|","+"
        def row(vals): return v+v.join(f"{p}{v2:<{w}}{p}" for v2,w in zip(vals,widths))+v
        border=tl+join.join(h*(w+2*self.padding) for w in widths)+tr
        return "\n".join([border,row(self.headers),border.replace(tl,join).replace(tr,join)]+[row(r) for r in self.rows]+[bl+h*(len(border)-2)+br])
    def show(self): self.stream.write(self.render()+"\n"); self.stream.flush(); return self

class Panel:
    def __init__(self,content,title=None,width=None,style="rounded",padding=1,stream=None):
        self.content=str(content); self.title=title; self.width=width; self.style=style; self.padding=max(0,int(padding)); self.stream=stream or sys.stdout
    def render(self):
        lines=self.content.splitlines() or [""]; width=self.width or max(len(x) for x in lines)+self.padding*2+2
        inner=max(1,width-self.padding*2-2)
        if self.style=="double": tl,tr,bl,br,h,v="╔","╗","╚","╝","═","║"
        elif self.style=="ascii": tl,tr,bl,br,h,v="+","+","+","+","-","|"
        else: tl,tr,bl,br,h,v="╭","╮","╰","╯","─","│"
        top=tl+h*(width-2)+tr
        if self.title: top=tl+" "+self.title[:max(0,width-4)]+" "+h*max(0,width-4-len(self.title))+tr
        body=[v+" "*self.padding+x[:inner].ljust(inner)+" "*self.padding+v for x in lines]
        return "\n".join([top]+body+[bl+h*(width-2)+br])
    def show(self): self.stream.write(self.render()+"\n"); self.stream.flush(); return self

class Tree:
    def __init__(self,root="Root",stream=None): self.root=str(root); self.children=[]; self.stream=stream or sys.stdout
    def add(self,path):
        node=self.children
        for part in str(path).strip("/").split("/"):
            found=next((x for x in node if x[0]==part),None)
            if not found: found=[part,[]]; node.append(found)
            node=found[1]
        return self
    def render(self):
        out=[self.root]
        def walk(nodes,prefix=""):
            for i,(name,kids) in enumerate(nodes):
                last=i==len(nodes)-1; out.append(prefix+("└── " if last else "├── ")+name); walk(kids,prefix+("    " if last else "│   "))
        walk(self.children); return "\n".join(out)
    def show(self): self.stream.write(self.render()+"\n"); self.stream.flush(); return self

class MultiMenu:
    def __init__(self,items,title="Select options",allow_quit=True,clear=False): self.items=items; self.title=title; self.allow_quit=allow_quit; self.clear=clear
    def show(self):
        items=list(self.items.items()) if isinstance(self.items,dict) else [(str(x),x) for x in self.items]; selected=set()
        while True:
            if self.clear: os.system("cls" if os.name=="nt" else "clear")
            print(f"\n=== {self.title} ===")
            for i,(label,_) in enumerate(items,1): print(f"[{ 'x' if i in selected else ' ' }] {i}. {label}")
            answer=input("Numbers separated by commas, 'done' to finish"+(", 'q' to quit" if self.allow_quit else "")+": ").strip().lower()
            if self.allow_quit and answer in {"q","quit","exit"}: return None
            if answer in {"done","d",""}: return [items[i-1][1] for i in sorted(selected)]
            try:
                selected={int(x.strip()) for x in answer.split(",") if x.strip()}; assert all(1<=i<=len(items) for i in selected)
            except (ValueError,AssertionError): print("Invalid selection.")

class Dashboard:
    def __init__(self,title="Dashboard",stream=None): self.title=title; self.values={}; self.stream=stream or sys.stdout
    def add(self,name,value): self.values[str(name)]=value; return self
    set=add
    def render(self): return "\n".join([self.title,"="*len(self.title)]+[f"{k}: {v}" for k,v in self.values.items()])
    def show(self,clear=True):
        if clear: os.system("cls" if os.name=="nt" else "clear")
        self.stream.write(self.render()+"\n"); self.stream.flush(); return self
