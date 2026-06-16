---
type: social-topic-report
date: '2026-06-15'
topic: xr
lang: th
pair: xr.en.md
generated_at: '2026-06-15T04:35:23+00:00'
generator: social-daily-report v0.1
model: claude-opus-4-7
platforms:
- x
regions:
- global
post_count: 91
salience: 0.45
sentiment: neutral
confidence: 0.5
tags:
- xr
- apple-vision-pro
- meta-quest
- webxr
- spatial-computing
- unity
thumbnail: https://pbs.twimg.com/media/HKsvNWva0AE3gaP.jpg
translated_by: claude-sonnet-4-6
---

# XR / VR / AR — 2026-06-15

## TL;DR
- โพสต์ที่แชร์กันอย่างกว้างขวางอ้างว่า Google และ Meta ปล่อย joint model ที่ infer geometry ของฉากแบบ 360° ครบถ้วน (depth, normals, sky masks, metric depth) พร้อม code สาธารณะแล้ว [24] — ยังไม่ verify แต่เป็น item ที่มีความเกี่ยวข้องทางเทคนิคมากที่สุดในวันนี้
- Apple Vision Pro M5 วางจำหน่ายแล้ว พร้อม dual knit band ใหม่, Device Hub สำหรับเปิด app จาก Mac, immersive environment Thórsmörk, และ Siri ที่รู้จัก physical scene [39][15][12][31]
- Meta Quest 3S 128GB (open box) ราคา $178.49 — เหมาะสำหรับ dev/demo hardware ราคาถูก [9]
- Developer รายหนึ่งสร้าง WebXR Snake ใน Unity รันบน Quest 3 ผลักดัน tabletop AR [13]; visionOS dev tooling (Low Level Texture API, RealityKit) ใช้งานจริงอยู่ [5][60]
- item ที่มี engagement สูงส่วนใหญ่เป็น noise — 'XR' หมายถึง iPhone XR เป็นหลัก [44][46][33] หรือ adult/crypto content [10][22][35]; signal XR จริงมีน้อย

## What happened
feed วันนี้ถูกครอบงำโดย Apple Vision Pro บนชิป M5 ในช่วงหลัง WWDC26 ผู้ใช้รายงาน dual knit band ใหม่ [39], Device Hub สำหรับเปิด Vision Pro app จาก Mac เพื่อ demo ได้ง่ายขึ้น [15], immersive environment Thórsmörk ใหม่ [12], Siri รู้จัก physical world ('what's in front of me') [31], flight environment M5 [25], และ AirDraw app ที่แปลงภาพวาด 3D เป็น object พิมพ์ได้ [32] Developer อ้างถึง visionOS API ที่ใช้งานจริง — Low Level Texture API สำหรับ caustics [5] และ RealityKit สำหรับ VivaTech demo [60] ด้านแพลตฟอร์ม มีโพสต์ยอดนิยมอ้างว่า Google และ Meta ปล่อย joint model สำหรับ 360° scene geometry ครบถ้วนพร้อม code สาธารณะ [24] Quest hardware ปรากฏผ่านดีล Quest 3S open-box ที่ $178.49 [9] และ Quest Pro พร้อม VR field-trip subscription [16] มี WebXR Snake demo ที่สร้างใน Unity รันบน Quest 3 [13] research items ได้แก่ touchable hologram ของ UPNA ที่ 2,880 images/sec [6], ความก้าวหน้าของ transparent OLED electrode [45], และงานวิจัย VR เรื่อง hazard assessment ของเด็ก [53]

## Why it matters (reasoning)
signal ที่สำคัญสำหรับ XR studio กระจุกอยู่สามจุด: Vision Pro tooling ที่ shipping แล้ว, การปล่อย spatial-perception model ที่อาจเป็นจริง, และ Quest hardware ราคาถูก Device Hub ของ Vision Pro [15] และงาน RealityKit/Low Level Texture [60][5] บ่งชี้ว่า visionOS toolchain สุกพอสำหรับ demo ปกติและ content effect — เกี่ยวข้องหาก NDF DEV รับงาน Apple spatial Google/Meta 360° geometry model พร้อม code สาธารณะ [24] ถ้าเป็นจริง จะลด cost ของ AR occlusion, placement และ reconstruction pipeline ที่ studio ต้องสร้างเองลงได้ — แต่มาจากบัญชีที่ชอบ hype จึงควรถือเป็น lead ที่ต้อง verify ไม่ใช่ข้อเท็จจริง Quest 3S ที่ $178 [9] ยังคงทำให้ Meta path เป็นทางเข้าที่ถูกที่สุดสำหรับ client demo และ edutech pilot [16][53] อีกนัยหนึ่ง: traffic คำว่า 'XR' ส่วนใหญ่เป็น iPhone XR และ adult/crypto noise [44][33][10][35] แสดงว่า social engagement เป็น proxy ที่แย่สำหรับความเกี่ยวข้องในฝั่ง XR developer — กรองด้วย source ไม่ใช่ score

## Possibility
มีแนวโน้มสูง: visionOS dev tooling ของ Vision Pro M5 จะค่อยๆ ดีขึ้นต่อเนื่อง และ visionOS content/environment ใหม่จะออกมาเรื่อยๆ เมื่อดูจาก first-party feature ที่ไหลมาอย่างสม่ำเสมอในรอบนี้ [12][15][31] เป็นไปได้: Google/Meta 360° geometry model เป็นของจริงและนำไปใช้กับ AR depth/occlusion ได้ แต่ต้อง verify repo และ license ก่อนวางแผนใดๆ [24] เป็นไปได้: แรงกดดันด้านราคา Quest ที่ลดลงต่อเนื่องจะขยายฐาน install base สำหรับ cheap demo [9] โอกาสกระทบ near-term ต่ำสำหรับ touchable hologram [6] และ transparent OLED [45] — ทั้งคู่ยังเป็น lab-stage research โดยไม่มี product path ที่ระบุไว้

## Org applicability — NDF DEV
1) Verify Google/Meta 360° geometry model [24] — หา repo จริง, license และ input ที่ต้องการ; ถ้าใช้ได้จริง ทดสอบกับ AR occlusion/placement ใน Unity/WebXR prototype (effort: med) 2) ซื้อ Quest 3S ราคา open-box สำหรับ demo/test hardware [9] (effort: low) 3) ต่อยอด pattern WebXR-Snake-ใน-Unity-บน-Quest [13] ให้เป็น tabletop-AR edutech demo เล็กๆ — ตรงกับแนว Unity + WebXR + e-learning ของ NDF DEV โดยตรง (effort: low-med) 4) ถ้าจะทำงาน Apple spatial ให้ใช้ Device Hub Mac-launch flow สำหรับ client demo [15] และประเมิน RealityKit/Low Level Texture API [60][5] (effort: med) 5) บันทึก VR field-trip [16] และงานวิจัย VR risk-play [53] ไว้เป็นหลักฐานสนับสนุนเมื่อ pitch VR ให้กับลูกค้า education (effort: low) ข้ามไปได้: โพสต์ XR โรงเรียนรัฐบาล Tamil Nadu [1][8] (คลุมเครือ, ตลาดต่างประเทศ, อ้างจาก fan-account), iPhone XR, crypto/$BASEY และ adult-VR ทั้งหมด [44][35][10] (ไม่เกี่ยวข้อง), และอย่าถือว่า tweet เดี่ยวใดยืนยันข้อเท็จจริงได้

## Signals to Watch
- ยืนยันว่า Google/Meta 360° scene-geometry model และ code สาธารณะมีอยู่จริง และ license เป็นอย่างไร [24]
- Cadence ของ Vision Pro M5 tooling หลัง WWDC26 — Device Hub, RealityKit update, Siri scene recognition [15][60][31]
- ราคา Quest 3S ในตลาดที่มีแนวโน้มลงสู่ ~$180 ลด cost ของ demo hardware [9]
- VR press อิสระ: เว็บไซต์ 'Good Virtual Reality' ของ Ian Hamilton ในฐานะแหล่งข่าว [21]

## Raw Sources
| platform | author | engagement | url |
|---|---|---|---|
| x | VijayFansTrends | ^962 c2 | [Looking Forward To Bringing Gaming, Animation, XR And Digital Content Creation I](https://x.com/VijayFansTrends/status/2065695471549755678) |
| x | views_ck10 | ^904 c58 | [Real Name: Kaitlin Trujillo Stage Name: Tru Kait Date of Birth: September 11, 19](https://x.com/views_ck10/status/2065796794127405383) |
| x | BenGeskin | ^556 c12 | [Even after more than two years of using it, Apple Vision Pro still impresses me ](https://x.com/BenGeskin/status/2066224162452980039) |
| x | BasedBiohacker | ^463 c17 | [nootropics ranking tier list, all compounds explained: S TIER: > bromantane: upr](https://x.com/BasedBiohacker/status/2066180939936412054) |
| x | doomdave | ^293 c10 | [You can use Animated Texture resource with Projective Textures. Here I have crea](https://x.com/doomdave/status/2065870618697019453) |
| x | AstronomyVibes | ^293 c22 | [🚨 Researchers at the Public University of Navarre (UPNA) have developed a ground](https://x.com/AstronomyVibes/status/2066021243552448679) |
| x | fwedesignerx | ^271 c26 | [I dey use xr and I get girlfriend 💔](https://x.com/fwedesignerx/status/2066211891274269004) |
| x | shivanandysky | ^253 c4 | [Honored to meet Hon. Minister for School Education, Tamil Development, Informati](https://x.com/shivanandysky/status/2065692289876521078) |
| x | Wario64 | ^236 c11 | [Meta Quest 3S 128GB - All-in-One Headset (Open Box) is $178.49 on Woot https://t](https://x.com/Wario64/status/2065814700374237303) |
| x | badbunnyxn | ^220 c5 | [Stop jerking to pics. Create the guy &amp; fuck him live on video call or in ful](https://x.com/badbunnyxn/status/2066059517457215511) |
| x | amrhsn | ^212 c3 | [@zolge1 This one as well... It really changed my life. I work in Mixed Reality b](https://x.com/amrhsn/status/2066118102429880485) |
| x | justinryanio | ^204 c6 | [The new immersive environment, Thórsmörk, on Apple Vision Pro is the best one ye](https://x.com/justinryanio/status/2066107363258474603) |
| x | dannyaroslavski | ^187 c8 | [Mini project this weekend : WebXR Snake. Built in Unity, running on Quest 3. Tho](https://x.com/dannyaroslavski/status/2065945355100078398) |
| x | ash_twtz | ^182 c59 | [iPhone Models and Their Release Year • 🍏 iPhone - 2007 • 🌐 iPhone 3G - 2008 • 🚀 ](https://x.com/ash_twtz/status/2066034154169565320) |
| x | xchester16 | ^168 c5 | [Playing around with the new Device Hub and found a nice surprise: we can now lau](https://x.com/xchester16/status/2065794821965627819) |
| x | sutosain | ^165 c1 | [I just received Meta Quest Pro Headset with Virtual Reality Field Trips 1-Month ](https://x.com/sutosain/status/2065862019249508804) |
| x | _belikebaddy | ^162 c55 | [Onedosh carry IPhone 17 pro max give Carter Efe make e share for live, make nobo](https://x.com/_belikebaddy/status/2065766484958163226) |
| x | smartbackwards | ^136 c5 | [we're saying goodbye to PARIVISION, but hello to a project i've had on the backb](https://x.com/smartbackwards/status/2065871586037727270) |
| x | TinaDebove | ^135 c6 | [Konate LOVES his Vision Pro https://t.co/K7DY296VTa](https://x.com/TinaDebove/status/2065809511147852250) |
| x | Arnoldruski | ^116 c19 | [Only hot thing in the 4 picture is the xr btw](https://x.com/Arnoldruski/status/2066097702081880265) |
| x | plectrumxr | ^102 c1 | [I was interviewed by Ian Hamilton, for his new independent VR journalism website](https://x.com/plectrumxr/status/2066075497881371007) |
| x | OliviaSparkleXX | ^99 c2 | [🔞‼️Yesterday, it was rainy in Prague, so we went to Jakkuyi shoot video... Do yo](https://x.com/OliviaSparkleXX/status/2065777151115239508) |
| x | CyberSeaNFT | ^86 c11 | [Code Is Art × CODE This is what the project is really about. To showcase what co](https://x.com/CyberSeaNFT/status/2065723460643430823) |
| x | RoundtableSpace | ^85 c12 | [Google and Meta just dropped a joint AI model that understands full 360° scene g](https://x.com/RoundtableSpace/status/2066245539188945376) |
| x | JonOrcera | ^82 c1 | [Best Vision Pro M5 flight "San Francisco✈️ New York" #WWDC26 https://t.co/9rHDDY](https://x.com/JonOrcera/status/2066193855691555328) |
| x | las91214 | ^80 c2 | [#BIRD_BINARY XR、SHADOW TROOPS EXの後、BIRD/BINARYはすっかり見込み薄い企画と見なされるようになりました。長年低予算で運](https://x.com/las91214/status/2065962554510500077) |
| x | Col2Vintage | ^77 c4 | [1979 Mercury Cougar XR-7 Dope or Nope 🤔 https://t.co/pLuHChc1nO](https://x.com/Col2Vintage/status/2066163750529335480) |
| x | SoundsLikeRonen | ^77 c4 | [I HAVE A BIG OFFER FOR YOU I decided to start making short video editing commiss](https://x.com/SoundsLikeRonen/status/2066059221460828396) |
| x | NightSkyNow | ^73 c20 | [🚨 What If Your Entire Life… Is Just Code? In 2003, philosopher Nick Bostrom publ](https://x.com/NightSkyNow/status/2065880692287045788) |
| x | GreekReporterr | ^71 c2 | [🇬🇷 Made in Hellas: The Greek Defence Company Behind Thousands of NATO Night Visi](https://x.com/GreekReporterr/status/2066254652530700423) |


## โพสต์เด่น

<div class="post-stream">
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@VijayFansTrends</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 962 · 💬 2</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/VijayFansTrends/status/2065695471549755678">View @VijayFansTrends on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Looking Forward To Bringing Gaming, Animation, XR And Digital Content Creation Into Government Schools 🎮🚀 Helping Students Learn, Create And Innovate For The Future 📚 @imrajmohan @TVKVijayHQ @shivanan”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>แฟนคลับนักการเมืองทมิฬโพสต์หวังให้รัฐบาลนำ gaming, animation, XR เข้าโรงเรียนรัฐใน Tamil Nadu — ยังไม่มีนโยบายหรือโปรแกรมจริงประกาศ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/VijayFansTrends/status/2065695471549755678" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@views_ck10</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 904 · 💬 58</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/views_ck10/status/2065796794127405383">View @views_ck10 on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Real Name: Kaitlin Trujillo Stage Name: Tru Kait Date of Birth: September 11, 1997 Age: 28 years old Birthplace: Long Beach, California, United States Nationality: American Profession: A#dult Film Act”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์นี้เป็นโปรไฟล์ของ adult content creator ไม่มีเนื้อหาด้าน XR หรือ tech ใดๆ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/views_ck10/status/2065796794127405383" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@BenGeskin</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 556 · 💬 12</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/BenGeskin/status/2066224162452980039">View @BenGeskin on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Even after more than two years of using it, Apple Vision Pro still impresses me ✨ https://t.co/2PLX9JJmHJ”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>ผู้ใช้ Apple Vision Pro แชร์ความรู้สึกว่ายังคง impress หลังใช้งานมากกว่า 2 ปี โดยไม่ได้ระบุ feature หรืออัปเดตใดเป็นพิเศษ</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/BenGeskin/status/2066224162452980039" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@BasedBiohacker</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 463 · 💬 17</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/BasedBiohacker/status/2066180939936412054">View @BasedBiohacker on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“nootropics ranking tier list, all compounds explained: S TIER: &gt; bromantane: upregulates tyrosine hydroxylase, increasing dopamine synthesis capacity at a genetic level &gt; pinealon: crosses nuclear mem”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>@BasedBiohacker โพสต์ tier list nootropics ส่วนตัว จัดอันดับสาร เช่น modafinil, bromantane, armodafinil ตามความเห็นผู้เขียน ไม่มีงานวิจัยอ้างอิง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/BasedBiohacker/status/2066180939936412054" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@doomdave</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 293 · 💬 10</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/doomdave/status/2065870618697019453">View @doomdave on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“You can use Animated Texture resource with Projective Textures. Here I have created this caustics effect in my Apple Vision Pro app using a Low Level Texture API released last year on VisionOS. The Or”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>Developer ใช้ VisionOS Low Level Texture API ร่วมกับ Animated Texture และ Projective Textures สร้าง caustics effect แบบ real-time พร้อม Bloom Component บน Apple Vision Pro</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>เทคนิค caustics นี้ใช้ได้กับ visionOS app ที่ต้องการ dynamic environmental lighting โดยไม่ต้องเขียน shader หนัก</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ทีม XR ลอง prototype caustics + Bloom pattern นี้ใน visionOS sandbox scene เพื่อเพิ่ม water หรือ light effect ระดับ production</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/doomdave/status/2065870618697019453" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@AstronomyVibes</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 293 · 💬 22</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/AstronomyVibes/status/2066021243552448679">View @AstronomyVibes on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“🚨 Researchers at the Public University of Navarre (UPNA) have developed a groundbreaking touchable hologram that can be physically felt. The system projects 2,880 images per second, creating the illus”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักวิจัย UPNA สร้างระบบ hologram สัมผัสได้โดยไม่ต้องใส่ถุงมือ ใช้คลื่น ultrasonic ฉาย 2,880 fps ให้ผู้ใช้รู้สึก pressure, texture และ motion บนวัตถุ 3D</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>Haptics ไม่ต้องใส่อุปกรณ์ตัดปัญหาใหญ่สุดใน XR presence และความก้าวหน้านี้บอกว่า hardware gap กำลังปิดลงนอก lab ยักษ์ใหญ่</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">อ้างอิงงานวิจัยนี้ตอน scope haptic interaction สำหรับ XR medical training หรือ industrial simulation เพื่อสนับสนุน design decision เรื่อง controller-free input</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/AstronomyVibes/status/2066021243552448679" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@fwedesignerx</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 271 · 💬 26</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/fwedesignerx/status/2066211891274269004">View @fwedesignerx on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“I dey use xr and I get girlfriend 💔”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>โพสต์ตลกว่าเล่น XR แล้วแฟนทิ้ง</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/fwedesignerx/status/2066211891274269004" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
<article class="ndf-card platform-x">
  <header class="ndf-card-head">
    <span class="ndf-author">@shivanandysky</span>
    <span class="ndf-platform">x</span>
    <span class="ndf-engagement">♥ 253 · 💬 4</span>
  </header>
  <blockquote class="twitter-tweet ndf-x-embed" data-dnt="true"><a href="https://x.com/shivanandysky/status/2065692289876521078">View @shivanandysky on X</a></blockquote>
  <div class="ndf-card-body">
    <p class="ndf-quote">“Honored to meet Hon. Minister for School Education, Tamil Development, Information &amp; Publicity, Government of Tamil Nadu, Thiru @imrajmohan Anna. We had an insightful discussion on empowering the next”</p>
    <dl class="ndf-fields">
      <dt>เนื้อหา</dt>
      <dd>นักการศึกษาด้าน XR/Animation เข้าพบรัฐมนตรีกระทรวงศึกษาของรัฐทมิฬนาฑู เพื่อหารือเรื่องการนำ Gaming, Animation และ XR เข้าสู่หลักสูตรนักเรียน</dd>
      <dt>ทำไมน่าสนใจ</dt>
      <dd>ไม่เกี่ยวข้อง</dd>
      <dt class="ndf-adapt-label">ใช้กับ NDF DEV ยังไง</dt>
      <dd class="ndf-adapt">ไม่มี action</dd>
    </dl>
    <a class="ndf-source" href="https://x.com/shivanandysky/status/2065692289876521078" target="_blank" rel="noopener">เปิดบน x →</a>
  </div>
</article>
</div>
