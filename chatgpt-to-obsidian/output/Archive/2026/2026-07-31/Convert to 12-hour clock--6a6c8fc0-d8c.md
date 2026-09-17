---
type: "chatgpt-conversation"
source: "ChatGPT export"
conversation_id: "6a6c8fc0-d8c4-83e8-9380-16114225537e"
created: 1785499614.980135
updated: 1785500357.089742
resource_section: true
---

# Convert to 12-hour clock

## User

\[Rainmeter\]
Update=10000
AccurateText=1
DynamicWindowSize=1

\[Variables\]
Scale=1

\[MeasureHour\]
Measure=Time
Format=%I

\[MeasureMinute\]
Measure=Time
Format=%M

\[MeasureTime\]
Measure=Time
Format=%H:%M


\[MeterTime\]
MeasureName=MeasureTime
Meter=STRING
X=0
Y=0
FontSize=80
FontColor=e2201f
FontFace=E1
AntiAlias=1
DynamicVariables=1

\[MeterTime2\]
MeasureName=MeasureTime
Meter=STRING
X=0
Y=0
FontSize=80
FontColor=ffffff
FontFace=E2
AntiAlias=1
DynamicVariables=1

convtert this clock to 12 hour format

## Assistant

Your Rainmeter skin is already measuring the hour in 12-hour format (`MeasureHour`), but `MeterTime` is using `MeasureTime`, which is defined as `%H:%M` (24-hour).

To convert it to a **12-hour clock**, change `MeasureTime` to use `%I:%M %p`.

```ini
\[Rainmeter\]
Update=10000
AccurateText=1
DynamicWindowSize=1

\[Variables\]
Scale=1

\[MeasureTime\]
Measure=Time
Format=%I:%M %p

\[MeterTime\]
MeasureName=MeasureTime
Meter=STRING
X=0
Y=0
FontSize=80
FontColor=e2201f
FontFace=E1
AntiAlias=1
DynamicVariables=1

\[MeterTime2\]
MeasureName=MeasureTime
Meter=STRING
X=0
Y=0
FontSize=80
FontColor=ffffff
FontFace=E2
AntiAlias=1
DynamicVariables=1
```

### Format codes
- `%H` → 24-hour (00–23)
- `%I` → 12-hour (01–12)
- `%M` → Minutes
- `%p` → `AM` / `PM`

If you want the clock to display **without the AM/PM suffix**, use:

```ini
Format=%I:%M
```

instead.

## User

write the same styling for %p

## Assistant

Since `%p` (AM/PM) is part of the same measure, you can't apply a different font or color to it within a single `STRING` meter. To style it separately, create a dedicated measure and meter.

```ini
\[MeasureTime\]
Measure=Time
Format=%I:%M

\[MeasureAMPM\]
Measure=Time
Format=%p

\[MeterTime\]
MeasureName=MeasureTime
Meter=STRING
X=0
Y=0
FontSize=80
FontColor=e2201f
FontFace=E1
AntiAlias=1
DynamicVariables=1

\[MeterTime2\]
MeasureName=MeasureTime
Meter=STRING
X=0
Y=0
FontSize=80
FontColor=ffffff
FontFace=E2
AntiAlias=1
DynamicVariables=1

; AM/PM shadow
\[MeterAMPM\]
MeasureName=MeasureAMPM
Meter=STRING
X=340
Y=22
FontSize=28
FontColor=e2201f
FontFace=E1
AntiAlias=1
DynamicVariables=1

; AM/PM foreground
\[MeterAMPM2\]
MeasureName=MeasureAMPM
Meter=STRING
X=340
Y=22
FontSize=28
FontColor=ffffff
FontFace=E2
AntiAlias=1
DynamicVariables=1
```

Adjust these values to suit your layout:
- `X=340` → Move the AM/PM text left or right.
- `Y=22` → Move it up or down.
- `FontSize=28` → Increase or decrease the AM/PM size.

This preserves the same dual-layer styling (red shadow + white foreground) that you're already using for the time.

## User

looks like this, style didnt apply to text pm

## Assistant

The issue is that your font (`E1`/`E2`) likely **doesn't contain glyphs for the letters `A`, `M`, or `P`**. Rainmeter falls back to another font (probably Segoe UI), so the custom styling only applies to the digits.

Your screenshot shows:
- ✅ Digits (`05:18`) rendered with your custom font.
- ❌ `PM` rendered in the fallback Windows font.

### Solution 1 (Recommended): Use a different font for AM/PM

```ini
\[MeterAMPM\]
MeasureName=MeasureAMPM
Meter=STRING
X=340
Y=20
FontFace=Segoe UI
FontSize=28
FontColor=e2201f
AntiAlias=1

\[MeterAMPM2\]
MeasureName=MeasureAMPM
Meter=STRING
X=340
Y=20
FontFace=Segoe UI
FontSize=28
FontColor=ffffff
AntiAlias=1
```

---

### Solution 2: Check your font

Open **Character Map** (`charmap.exe`), select `E1` or `E2`, and see whether it contains the letters **A, M, P**.

If those letters are missing, there is no way for Rainmeter to render `AM`/`PM` in that font.

---

### Solution 3: Use a font with matching aesthetics

If you want the `AM`/`PM` to match the futuristic style, choose a font that includes alphabetic characters, such as:
- Orbitron
- Michroma
- Rajdhani
- Eurostile
- Bank Gothic

---

**Question:** Is `E1`/`E2` a custom digital font (like from dafont.com), or is it a font you created yourself?

## User

reduce the size of this battry widget entirly by 50%

## Assistant

Sure—please paste the **Rainmeter battery widget (`.ini`) code** here.

To reduce the **entire widget by 50%**, I'll:
- Halve all `X` and `Y` positions.
- Halve all `W`/`H` (width/height) values.
- Halve all `FontSize` values.
- Halve `LineWidth`, `SolidColor` dimensions, `Shape` sizes, and any image dimensions.
- Keep the layout and proportions exactly the same.

If the skin already uses a variable like:

```ini
\[Variables\]
Scale=1
```

I can also make it scalable so you only need to change **one line**:

```ini
\[Variables\]
Scale=0.5
```

and every element will automatically resize.

Just paste the `.ini` file, and I'll convert it to a fully scalable 50% version.

## User

\[Metadata\]
Author=Sahil / MaybeSahil / Runixe786
Name=NothingOS clock
Description=NothingOS inspired clock widget for Windows
Tags=clock ,windows ,android ,NothingUI ,material

\[Rainmeter\]
Update=10000
AccurateText=1
DynamicWindowSize=1

\[Variables\]
@IncludeVar=#@#Settings.inc
batlvl=(\[MeterRound:W\]/3)
batlvlhide=(\[MeterRound:W\]/2)
Scale=1
Size=190
Radius=(#Size#/2)
BgColor=0,0,0,255
BatteryColor=255,0,0,255
BatRemainingMsg=wait..

\[MeasureBattery\]
Measure=Plugin
Plugin=PowerPlugin
PowerState=Percent


\[background\]
Meter=Shape
X=100
Y=100
Shape= Ellipse 0,0,95,95,25 | StrokeWidth 0 | FillColor 303038

\[MeterBatteryPie\]
Meter=Roundline
MeasureName=MeasureBattery
X=5
Y=5
W=190
H=190
StartAngle=(Rad(270))
RotationAngle=(Rad(360))
LineStart=0
LineLength=#Radius#
Solid=1
AntiAlias=1
LineColor=E2201F
DynamicVariables=1


\[background1\]
Meter=Shape
X=100
Y=100
Shape= Ellipse 0,0,85,85,25 | StrokeWidth 0 | FillColor 1B1C1D

\[MeasureBatteryPercent\]
Measure=Plugin
Plugin=PowerPlugin
PowerState=Percent
IfCondition=(MeasureBatteryPercent <= 30)
IfTrueAction=\[!SetOption MeterBackground "ImageName" "#@#low.PNG"\]\[!Redraw\]
IfCondition2=(MeasureBatteryPercent >= 31) && (MeasureBatteryPercent <=80)
IfTrueAction2=\[!SetOption MeterBackground "ImageName" "#@#mid.PNG"\]\[!Redraw\]
IfCondition3=(MeasureBatteryPercent >= 81)
IfTrueAction3=\[!SetOption MeterBackground "ImageName" "#@#full.PNG"\]\[!Redraw\]

\[MeterBackground\]
Meter=Image
ImageName=#@#full.PNG
DynamicVariables=1
X=60
Y=40
H=80
W=80

\[MeasureBattery\]
Measure=Plugin
Plugin=PowerPlugin
PowerState=Percent
PowerState=Charging
DynamicVariables=1

\[MeterBatteryPercent\]
Meter=String
MeasureName=MeasureBattery
FontFace=Nothing Font (5x7)
FontColor=F1F0F6
FontSize=16
StringAlign=CENTERCENTER
AntiAlias=1
X=100
Y=142
Text="%1%"
DynamicVariables=1

## Assistant

The cleanest way is to keep the proportions the same and scale every coordinate and size by **0.5**.

Here's your widget at **50% of its original size**:

```ini
\[Metadata\]
Author=Sahil / MaybeSahil / Runixe786
Name=NothingOS Battery
Description=NothingOS inspired battery widget for Windows

\[Rainmeter\]
Update=10000
AccurateText=1
DynamicWindowSize=1

\[Variables\]
@IncludeVar=#@#Settings.inc
Scale=0.5
Size=(190*#Scale#)
Radius=(#Size#/2)

BgColor=0,0,0,255
BatteryColor=255,0,0,255

\[MeasureBattery\]
Measure=Plugin
Plugin=PowerPlugin
PowerState=Percent

;==================== OUTER CIRCLE ====================

\[background\]
Meter=Shape
X=(100*#Scale#)
Y=(100*#Scale#)
Shape=Ellipse 0,0,(95*#Scale#),(95*#Scale#),25 | StrokeWidth 0 | FillColor 303038

\[MeterBatteryPie\]
Meter=Roundline
MeasureName=MeasureBattery
X=(5*#Scale#)
Y=(5*#Scale#)
W=#Size#
H=#Size#
StartAngle=(Rad(270))
RotationAngle=(Rad(360))
LineStart=0
LineLength=#Radius#
Solid=1
AntiAlias=1
LineColor=E2201F
DynamicVariables=1

;==================== INNER CIRCLE ====================

\[background1\]
Meter=Shape
X=(100*#Scale#)
Y=(100*#Scale#)
Shape=Ellipse 0,0,(85*#Scale#),(85*#Scale#),25 | StrokeWidth 0 | FillColor 1B1C1D

;==================== BATTERY ICON ====================

\[MeasureBatteryPercent\]
Measure=Plugin
Plugin=PowerPlugin
PowerState=Percent

IfCondition=(MeasureBatteryPercent<=30)
IfTrueAction=\[!SetOption MeterBackground ImageName "#@#low.PNG"\]\[!Redraw\]

IfCondition2=(MeasureBatteryPercent>=31)&&(MeasureBatteryPercent<=80)
IfTrueAction2=\[!SetOption MeterBackground ImageName "#@#mid.PNG"\]\[!Redraw\]

IfCondition3=(MeasureBatteryPercent>=81)
IfTrueAction3=\[!SetOption MeterBackground ImageName "#@#full.PNG"\]\[!Redraw\]

\[MeterBackground\]
Meter=Image
ImageName=#@#full.PNG
DynamicVariables=1
X=(60*#Scale#)
Y=(40*#Scale#)
W=(80*#Scale#)
H=(80*#Scale#)

;==================== PERCENT TEXT ====================

\[MeasureBatteryValue\]
Measure=Plugin
Plugin=PowerPlugin
PowerState=Percent

\[MeterBatteryPercent\]
Meter=String
MeasureName=MeasureBatteryValue
FontFace=Nothing Font (5x7)
FontColor=F1F0F6
FontSize=(16*#Scale#)
StringAlign=CENTERCENTER
AntiAlias=1
X=(100*#Scale#)
Y=(142*#Scale#)
Text="%1%"
DynamicVariables=1
```

### Notes
- The entire widget is now **exactly half the original size** (`Scale=0.5`).
- If you want it larger or smaller later, simply change:
 ```ini
 Scale=0.5
 ```
 to values like:
 - `0.75` → 75%
 - `0.6` → 60%
 - `1` → original size
 - `1.25` → 125%

This makes the widget fully scalable from a single variable.

## Resources

### Local attachments
- [image(56).png](../../../Raw/Export/file_000000004460820ba799ae16955f8089.dat)
