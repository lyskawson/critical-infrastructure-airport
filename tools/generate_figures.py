#!/usr/bin/env python3
"""Editable vector drawings. Run from any directory; Python 3 + reportlab."""
import json
import math
import os
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor, Color, white

ROOT = Path(__file__).resolve().parents[1]
D = json.loads((ROOT / "data/design.json").read_text())
if D.get("schema_version", 1) >= 2:
    raise SystemExit("Version 1 generator is disabled for model A. B rebuilds the drawings; register: make data.")
OUT = ROOT / "figures"
OUT.mkdir(exist_ok=True)
font_pairs = [
    (os.environ.get("PROJECT_FONT_REGULAR", ""), os.environ.get("PROJECT_FONT_BOLD", "")),
    ("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"),
    ("/System/Library/Fonts/Supplemental/Arial.ttf", "/System/Library/Fonts/Supplemental/Arial Bold.ttf"),
]
for reg, bold in font_pairs:
    if reg and Path(reg).is_file() and Path(bold).is_file():
        pdfmetrics.registerFont(TTFont("Project", reg))
        pdfmetrics.registerFont(TTFont("ProjectBold", bold))
        break
else:
    raise SystemExit("No Unicode font. Set PROJECT_FONT_REGULAR and PROJECT_FONT_BOLD.")

NAVY = HexColor("#132D46")
TEAL = HexColor("#087F8C")
BLUE = HexColor("#367EBC")
AMBER = HexColor("#BE7A17")
FIRE = HexColor("#B94646")
MUTED = HexColor("#526575")
MIST = HexColor("#EDF4F6")
GREEN = HexColor("#3D8765")
GRID = HexColor("#DCE6EB")

def label(c, x, y, s, size=18, color=NAVY, bold=False, align="left"):
    c.setFillColor(color)
    c.setFont("ProjectBold" if bold else "Project", size)
    getattr(c, {"left":"drawString", "center":"drawCentredString", "right":"drawRightString"}[align])(x,y,s)

def multiline(c,x,y,lines,size=18,color=NAVY,bold=False,align="center",leading=None):
    for i,line in enumerate(lines):
        label(c,x,y-i*(leading or size*1.38),line,size,color,bold,align)

def page(name,w,h,kicker):
    c=canvas.Canvas(str(OUT/name),pagesize=(w,h),pageCompression=1,invariant=1)
    c.setTitle(kicker)
    c.setAuthor("Academic project - North Airport")
    label(c,24,h-30,kicker,17,TEAL,True)
    return c

def box(c,x,y,w,h,lines,accent=TEAL,fill=MIST,size=18):
    c.setStrokeColor(accent); c.setFillColor(fill); c.setLineWidth(1.8)
    c.roundRect(x,y,w,h,10,stroke=1,fill=1)
    multiline(c,x+w/2,y+h/2+(len(lines)-1)*size*.68-size*.32,lines,size,accent,True)

def line(c,pts,color=TEAL,width=3,dash=None,arrow=False):
    c.setStrokeColor(color); c.setLineWidth(width)
    c.setDash(dash or [])
    p=c.beginPath(); p.moveTo(*pts[0])
    for pt in pts[1:]: p.lineTo(*pt)
    c.drawPath(p)
    c.setDash([])
    if arrow:
        x0,y0=pts[-2]; x1,y1=pts[-1]
        a=math.atan2(y1-y0,x1-x0)
        p=c.beginPath(); p.moveTo(x1,y1)
        for d in (.43,-.43):
            p.lineTo(x1-11*math.cos(a+d),y1-11*math.sin(a+d))
        p.close()
        c.setFillColor(color); c.drawPath(p,fill=1,stroke=0)

def architecture():
    c=page("architecture.pdf",1000,600,"01 / FUNCTIONAL ARCHITECTURE")
    for x in (155,500,845):
        line(c,[(x,466),(x,430),(500,430),(500,405)],BLUE,arrow=True)
    for x in (155,500,845):
        line(c,[(500,335),(500,302),(x,302),(x,280)],BLUE,arrow=True)
    line(c,[(235,125),(285,125)],FIRE,arrow=True)
    line(c,[(615,125),(690,125),(690,245),(735,245)],FIRE,dash=[8,5],arrow=True)
    box(c,35,466,240,76,["CCTV / 24 cameras","H.265 • PoE+"],BLUE)
    box(c,380,466,240,76,["ACS / 14 points","8 controllers"],BLUE)
    box(c,725,466,240,76,["IDS / 4 panels","IP + LTE channel"],BLUE)
    box(c,220,335,560,70,["SEGREGATED LAN / VLAN + FIREWALL","N0-N1-N2-N3-N0 • OS2 • RSTP"],BLUE,size=19)
    box(c,35,210,240,70,["VMS + recording","4 × 8 TB / RAID 6"],BLUE)
    box(c,380,210,240,70,["AI / 8 streams","local analytics"],BLUE)
    box(c,735,210,230,70,["SOC / 2 stations","event integration"],BLUE)
    box(c,35,78,200,94,["4 local FAS panels","detectors / MCPs","notification"],FIRE,HexColor("#FBF0F0"),17)
    box(c,285,78,330,94,["SEPARATE FAS NETWORK","manufacturer bus","local batteries and controls"],FIRE,HexColor("#FBF0F0"),17)
    label(c,706,113,"FAS gateway",16,FIRE)
    label(c,706,89,"read-only events",16,FIRE)
    label(c,35,30,"Local fire alarms operate independently of LAN, VMS, and AI.",17,MUTED)
    c.save()

def sitebase(c,route=False):
    # Same x and y scale: 1.36 drawing points per metre.
    scale=1.36; ox=75; oy=75
    def xy(x,y): return ox+x*scale,oy+y*scale
    c.setFillColor(HexColor("#F5F8F7")); c.rect(ox,oy,600*scale,400*scale,fill=1,stroke=0)
    for x in range(0,601,100):
        line(c,[xy(x,0),xy(x,400)],GRID,.6)
        label(c,*xy(x,-17),str(x),14,MUTED,align="center")
    for y in range(0,401,100):
        line(c,[xy(0,y),xy(600,y)],GRID,.6)
        px,py=xy(-12,y); label(c,px,py-4,str(y),14,MUTED,align="right")
    line(c,[xy(0,0),xy(600,0),xy(600,400),xy(0,400),xy(0,0)],NAVY,2)
    if not route:
        c.setFillColor(HexColor("#E5EDEF")); c.rect(*xy(160,160),340*scale,145*scale,fill=1,stroke=0)
        label(c,*xy(330,225),"APRON AREA",18,MUTED,True,align="center")
        label(c,*xy(330,206),"selected viewing directions",15,MUTED,align="center")
        c.setFillColor(HexColor("#E5EDEF")); c.rect(*xy(180,45),180*scale,30*scale,fill=1,stroke=0)
        label(c,*xy(270,55),"CAR PARK / ZONE A",15,MUTED,align="center")
    for n in D["nodes"]:
        x,y,w,h=n["rect"]
        c.setFillColor(HexColor("#BDCEDA")); c.setStrokeColor(NAVY)
        c.rect(*xy(x,y),w*scale,h*scale,fill=1,stroke=1)
    line(c,[(947,535),(947,595)],NAVY,2,arrow=True)
    label(c,947,614,"N",19,NAVY,True,align="center")
    label(c,947,506,"nominal",12,MUTED,align="center")
    line(c,[xy(0,-35),xy(100,-35)],NAVY,3)
    for x in (0,50,100): line(c,[xy(x,-38),xy(x,-32)],NAVY,1)
    label(c,*xy(110,-39),"100 m",14,MUTED)
    label(c,890,32,"x [m]",14,MUTED,align="right")
    label(c,27,643,"y [m]",14,MUTED)
    return xy

def site():
    c=page("site-plan.pdf",1000,710,"02 / SITE PLAN - FICTIONAL SITE")
    xy=sitebase(c)
    calls=[
        ("N0",25,175,["TERMINAL / SOC","C01-C08 indoors • C09-C10 outdoors","D01-D06 • CSP-0 • SSWiN-0"]),
        ("N1",160,290,["HANGAR","C11-C15 • D07-D09","CSP-1 • SSWiN-1"]),
        ("N2",365,312,["TECHNICAL","C16-C19 • D10-D11","CSP-2 • SSWiN-2"]),
        ("N3",420,114,["GATEHOUSE / GATES","C20-C24 • D12 • G01-G02","CSP-3 • SSWiN-3"])
    ]
    # Label callouts use open ground; exact node coordinates remain visible as circles.
    for nid,lx,ly,lines in calls:
        n=next(n for n in D["nodes"] if n["id"]==nid)
        px,py=xy(*n["xy"]); tx,ty=xy(lx,ly)
        end=(tx-9,ty-19) if px<tx else (tx,ty-58)
        line(c,[(px,py),end],MUTED,1.2)
        c.setFillColor(TEAL); c.circle(px,py,7,fill=1,stroke=0)
        multiline(c,tx,ty, [nid+" / "+lines[0]]+lines[1:],15,NAVY,align="left",leading=22)
    gx,gy=xy(495,215)
    c.setStrokeColor(AMBER); c.setFillColor(HexColor("#FCF3E2")); c.rect(gx,gy,32,18,fill=1,stroke=1)
    label(c,gx+16,gy+25,"GEN",13,AMBER,True,align="center")
    # Gate positions are symbolic, outside the runway and navigation scope.
    for x,t in [(500,"G01"),(550,"G02")]:
        px,py=xy(x,0); line(c,[(px-12,py),(px+12,py)],GREEN,5)
        label(c,px,py-43,t,13,GREEN,True,align="center")
    label(c,75,662,"24 ha / terminal • hangar • technical • gatehouse",17,MUTED)
    c.save()

def routes():
    c=page("routes.pdf",1000,710,"03 / FIBRE ROUTES - CONCEPT GEOMETRY")
    xy=sitebase(c,True)
    cols=[TEAL,BLUE,AMBER,FIRE]
    for r,col in zip(D["routes"],cols):
        line(c,[xy(*p) for p in r["points"]],col,5)
    tags=[(155,138),(270,355),(505,160),(365,19)]
    for r,col,(x,y) in zip(D["routes"],cols,tags):
        px,py=xy(x,y)
        label(c,px,py,f'{r["id"]} / {r["length_m"]} m',17,col,True)
    for n in D["nodes"]:
        px,py=xy(*n["xy"])
        c.setFillColor(NAVY); c.circle(px,py,9,fill=1,stroke=0)
        label(c,px+16,py-5,n["id"],20,NAVY,True)
    # 4 building chambers + 4 conceptual intermediate chambers (8 total).
    chambers=[n["xy"] for n in D["nodes"]]+[[100,120],[100,340],[560,240],[280,40]]
    for x,y in chambers:
        px,py=xy(x,y); c.setStrokeColor(NAVY); c.setLineWidth(1.5)
        c.rect(px-12,py-12,24,24,fill=0,stroke=1)
    label(c,75,660,"OS2 12-core: 2 LAN + 2 FAS + 8 spare fibres / sections R1-R4",17,MUTED)
    c.save()

def terminal():
    c=page("terminal.pdf",1000,595,"04 / TERMINAL - FUNCTIONAL PLAN 80 × 40 m")
    ox,oy,s=90,160,10
    def xy(x,y): return ox+x*s,oy+y*s
    rooms=[
        (0,0,30,25,"A / PUBLIC HALL",HexColor("#F0F5F6"),(15,12)),
        (0,25,30,15,"B / STAFF",HexColor("#EAF3EC"),(15,31)),
        (30,0,50,15,"A / ENTRANCE AND CIRCULATION",HexColor("#F0F5F6"),(55,7)),
        (30,15,20,10,"D / SOC",HexColor("#DDE9F2"),(40,21)),
        (30,25,20,15,"B / BACK OF HOUSE",HexColor("#EAF3EC"),(40,31)),
        (50,15,30,25,"C / OPERATIONS",HexColor("#FBF2E3"),(65,27))
    ]
    for x,y,w,h,title,color,txy in rooms:
        c.setFillColor(color); c.setStrokeColor(NAVY); c.setLineWidth(2)
        c.rect(*xy(x,y),w*s,h*s,fill=1,stroke=1)
        label(c,*xy(*txy),title,16,NAVY,True,align="center")
    # Local route examples, deliberately distinct from measured main trench routes.
    line(c,[xy(5,2),xy(5,20),xy(40,20),xy(75,20),xy(75,37)],BLUE,2,[6,4])
    line(c,[xy(2,2),xy(78,2),xy(78,38),xy(2,38),xy(2,2)],FIRE,1.5,[3,4])
    for row in range(6):
        for col in range(8):
            px,py=xy(5+10*col,3.333+6.667*row)
            c.setFillColor(FIRE); c.circle(px,py,3.2,fill=1,stroke=0)
    for i,(x,y) in enumerate(D["camera_terminal_xy"],1):
        px,py=xy(x,y)
        c.setFillColor(BLUE); c.circle(px,py,9,fill=1,stroke=0)
        dx=15 if x<70 else -15
        label(c,px+dx,py+10,f"C{i:02}",16,BLUE,True,align="left" if dx>0 else "right")
    doors=[(30,7),(15,25),(40,15),(50,20),(40,25),(50,32)]
    for i,(x,y) in enumerate(doors,1):
        px,py=xy(x,y)
        c.setStrokeColor(white); c.setLineWidth(12)
        c.line(px-9,py,px+9,py)
        c.setFillColor(GREEN); c.rect(px-6,py-6,12,12,fill=1,stroke=0)
        label(c,px+11,py-18,f"D{i:02}",14,GREEN,True)
    px,py=xy(40,18)
    label(c,px,py,"N0 / CSP-0",13,TEAL,True,align="center")
    line(c,[xy(0,-3),xy(80,-3)],NAVY,1.1)
    label(c,*xy(40,-5),"80 m",17,NAVY,align="center")
    line(c,[xy(-3,0),xy(-3,40)],NAVY,1.1)
    label(c,25,350,"40 m",17,NAVY)
    label(c,90,72,"● camera      ■ ACS point      • indicative fire detection (48 points)",18,MUTED)
    label(c,90,38,"Blue: IP route / red: FAS circuit concept. Discipline-specific design required.",16,MUTED)
    c.save()

def ai_flow():
    c=page("ai-flow.pdf",1000,240,"05 / AI SUPPORTS OPERATOR DECISIONS")
    xs=[25,280,535,790]
    titles=[["VIDEO","8 selected cameras"],["ML MODEL","objects + tracking"],["ZONE RULE","alarm candidate"],["OPERATOR","review + response"]]
    for i in range(3):
        line(c,[(xs[i]+185,132),(xs[i+1],132)],TEAL,3,arrow=True)
    for x,tt in zip(xs,titles): box(c,x,90,185,85,tt,size=17)
    label(c,25,35,"Pilot and TP / FP / FN measurement • local analysis • independent of FAS controls",18,MUTED)
    c.save()

def power():
    c=page("power.pdf",1000,440,"06 / POWER AND BACKUP")
    line(c,[(245,337),(350,337)],AMBER,arrow=True)
    line(c,[(245,232),(300,232),(300,320),(350,320)],AMBER,arrow=True)
    line(c,[(550,328),(655,328)],AMBER,arrow=True)
    line(c,[(775,292),(775,245),(445,245),(445,192)],AMBER,arrow=True)
    line(c,[(775,245),(775,192)],AMBER,arrow=True)
    box(c,25,300,220,76,["MAINS 230/400 V"],AMBER,size=19)
    box(c,25,194,220,76,["GENERATOR","10 kVA / 8 kW"],AMBER,size=19)
    box(c,350,292,200,84,["ATS","target: up to 60 s"],AMBER,size=19)
    box(c,655,292,280,84,["POWER DISTRIBUTION","security circuits"],AMBER,size=18)
    box(c,85,100,430,92,["UPS N0: 3 kVA + 3 × 1 kVA N1-N3","target: 30 min","IT / CCTV / SOC"],BLUE,size=17)
    box(c,560,100,405,92,["SEPARATE BACKUP SUPPLIES","FAS / ACS / IDS","local DC batteries"],FIRE,HexColor("#FBF0F0"),17)
    label(c,25,45,"Fire circuits and emergency-isolation arrangement follow the approved design.",17,MUTED)
    c.save()

def register():
    lines=["# Device assembly register", "", "Fictional site. Local coordinates are in metres, not surveyed points.", "", "| Node | (x,y) | Cameras | Doors / gates | FAS | IDS |", "|---|---|---|---|---|---|---|"]
    camera=door=1
    for n in D["nodes"]:
        count=n["fixed"]+n["ptz"]
        cams=f'C{camera:02}-C{camera+count-1:02}'
        doors=f'D{door:02}-D{door+n["doors"]-1:02}'
        if n["gates"]: doors+="; G01-G02"
        lines.append(f'| {n["id"]}: {n["name"]} | {n["xy"]} | {cams} | {doors} | {n["fire_detectors"]} detectors, {n["rop"]} MCPs | {n["pir"]} PIRs, {n["contacts"]} contacts |')
        camera+=count; door+=n["doors"]
    lines += ["", "Terminal cameras C01-C08 are shown individually. C09-C10 cover the entrance and apron facade. Other groups use fixed cameras for facades and access points; PTZ provides surrounding-area verification. Exact positions, heights, and views require field testing.", "", "FAS, ACS, and IDS identifiers must be assigned to actual rooms after plans are accepted. Counts in this legacy register are not verified detection coverage.", ""]
    (ROOT/"docs/device-register.md").write_text("\n".join(lines))

if __name__=="__main__":
    for fn in (architecture,site,routes,terminal,ai_flow,power,register): fn()
    print("Generated 6 vector PDF drawings and the assembly register.")
