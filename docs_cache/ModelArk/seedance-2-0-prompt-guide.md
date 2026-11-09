---
url: https://docs.byteplus.com/en/docs/ModelArk/seedance-2-0-prompt-guide
title: 'Dreamina Seedance 2.0 series prompt guide--ModelArk-Byteplus'
key: ModelArk/seedance-2-0-prompt-guide
---

ModelArk

DocumentCoding PlanAPI referenceResourcesAI Suite

###### ModelArk

ModelArk

Document

Search

Get started

[Overview](/docs/ModelArk/product-overview)

[Quick start](/docs/ModelArk/quick-start)

[Pricing](/docs/ModelArk/model-pricing)

[Region availability](/docs/ModelArk/region-availability)

[Best practices of model calling for agents](/docs/ModelArk/agent-model-invocation-practice)

[Migrate to the official Ark SDK](/docs/ModelArk/migrate-ark-runtime-sdk)

Model

[Model list](/docs/ModelArk/model-list)

[DeepSeek V4.1 Flash](/docs/ModelArk/deepseek-v4-1-flash)

Model invocation

[Text generation](/docs/ModelArk/text-generation)

Multi-modal understanding

[Image understanding](/docs/ModelArk/image-understanding)

[Video understanding](/docs/ModelArk/video-understanding)

[Document understanding](/docs/ModelArk/document-understanding)

[Audio understanding](/docs/ModelArk/audio-understanding)

Video generation

[Dreamina Seedance 2.5 tutorial](/docs/ModelArk/seedance-2-5)

[Dreamina Seedance 2.5 prompt guide](/docs/ModelArk/seedance-2-5-prompt-guide)

[Dreamina Seedance 2.0 series tutorial](/docs/ModelArk/seedance-2-0)

[Dreamina Seedance 2.0 series prompt guide](/docs/ModelArk/seedance-2-0-prompt-guide)

[Video generation tutorial](/docs/ModelArk/video-generation-tutorial)

[Create portrait videos with Dreamina Seedance models](/docs/ModelArk/seedance-portrait-asset-guide)

Image generation

[Seedream 5.0 pro / flash tutorial](/docs/ModelArk/seedream-5-0-pro)

[Seedream 5.0 pro / flash interactive editing guide](/docs/ModelArk/seedream-5-0-pro-editing-guide)

[Image generation tutorial](/docs/ModelArk/image-generation-tutorial)

Embeddings

[Multimodal embedding](/docs/ModelArk/vectorization)

Tool use

[Cloud-deployed MCP / remote MCP](/docs/ModelArk/mcp-remote-mcp)

[Function call](/docs/ModelArk/function-calling)

Advanced usage

[Deep reasoning](/docs/ModelArk/deep-thinking)

[Context management](/docs/ModelArk/context-management)

[Streaming output](/docs/ModelArk/streaming-output)

[Prefill-based response](/docs/ModelArk/continuation-mode)

[Context cache](/docs/ModelArk/context-cache)

[Files API tutorial](/docs/ModelArk/file-api)

[Visual grounding](/docs/ModelArk/grounding)

[Prompt engineering](/docs/ModelArk/prompt-engineering)

[Structured output (beta)](/docs/ModelArk/structured-output-beta)

[Integrate with third-party tools](/docs/ModelArk/integrate-third-party-tools)

Responses API tutorials

[Migrate to Responses API](/docs/ModelArk/responses-api-migration)

[Text generation (Responses API)](/docs/ModelArk/responses-api-text-generation)

[Deep reasoning (Responses API)](/docs/ModelArk/responses-api-deep-thinking)

[Multimodal understanding (Responses API)](/docs/ModelArk/multimodal-understanding)

[Tool use (Responses API)](/docs/ModelArk/responses-api-tool-calling)

[Structured output (Responses API)](/docs/ModelArk/responses-api-structured-output)

[Context editing (Responses API)](/docs/ModelArk/responses-api-context-editing)

Inference

[Inference methods overview](/docs/ModelArk/deployment-overview)

[Online inference (standard)](/docs/ModelArk/online-inference-standard)

[Online inference (Flex)](/docs/ModelArk/online-inference-flex)

Model Unit

[Model Unit](/docs/ModelArk/model-unit-overview)

[Batch inference](/docs/ModelArk/batch-inference)

Managed Agents

Get started

[Overview](/docs/ModelArk/overview)

[Quick start (code)](/docs/ModelArk/quick-start-code)

[Quick start (console)](/docs/ModelArk/quick-start-console)

Define agents

[Agent](/docs/ModelArk/define-agent)

[Skills](/docs/ModelArk/skills)

[MCP](/docs/ModelArk/mcp)

[Tools](/docs/ModelArk/tools)

[Tool permission policy](/docs/ModelArk/tool-permission-policy)

[List of parameters supported by models](/docs/ModelArk/model-parameter-support)

Configure agent environments

[Configure cloud environments](/docs/ModelArk/configure-cloud-environment)

[Cloud sandbox reference](/docs/ModelArk/cloud-sandbox-reference)

Self-hosted environments

[Self-hosted environment overview](/docs/ModelArk/self-hosted-environment-overview)

[Configure and run a self-hosted environment](/docs/ModelArk/configure-self-hosted-environment)

[Self-hosted environment security](/docs/ModelArk/self-hosted-environment-security)

Delegate tasks to agents

[Start session](/docs/ModelArk/start-session)

[Manage session](/docs/ModelArk/manage-session)

[Session event stream](/docs/ModelArk/session-event-stream)

[Receive webhook events](/docs/ModelArk/receive-webhook-events)

[Use Vaults authentication](/docs/ModelArk/use-vaults-authentication)

[Run and manage background tool tasks](/docs/ModelArk/background-tool-tasks)

Manage agent context

[Upload and mount files](/docs/ModelArk/upload-and-mount-files)

[Persistent memory](/docs/ModelArk/persistent-memory)

[Configure context compaction](/docs/ModelArk/context-compaction)

Advanced capabilities

[Multi Agent](/docs/ModelArk/multi-agent)

  * Home
ModelArkModel invocationVideo generationDreamina Seedance 2.0 series prompt guide

Copy Page

Video generation

Dreamina Seedance 2.0 series prompt guide

Copy Page

Dreamina Seedance 2.0 series prompt guide

Feedback

The Dreamina Seedance 2.0 series (Seedance 2.0 series) model natively supports joint audio and video generation, with excellent semantic understanding and multimodal interaction capabilities. This article introduces how to write prompts for the Seedance 2.0 series model and related tips, helping you use the model more efficiently to generate high-quality videos that meet your needs.​

Note​

All visual (image, video) and audio assets presented in this guide are autonomously generated by the Seedance/Seedream series visual generation models.​

Basic formula​

The Seedance 2.0 series model supports referencing multimodal assets such as videos, images, and audio at the same time. It can accurately lock in characteristics such as character appearance, action effects, visual style, and voice-over timbre, greatly lowering the threshold for writing prompts. Based on this advantage, we can guide the model with a simple basic formula, using the features of multimodal assets to quickly generate videos that meet specific requirements.​

Reference-based video generation can be subdivided into three types of tasks: omni reference, editing videos, and extending videos. You can choose the basic prompt formula according to the task type.​

Omni reference​

Extract some elements from the asset (such as subject, style, scene, and sound effects) to generate a brand-new video.​

  * Applicable scenarios: Action transfer, subject reuse, atmosphere reference, etc.​

  * Recommended patterns:​

  * Image reference: Reference <Subject_N> in <Image_N> to generate...​

  * Video reference: Reference <Action/Camera_movement/Style/Sound_effect> in <Video_N> to generate...​

  * Audio reference: Reference the timbre in <Audio_N> to generate...​

Video editing​

Make partial or global modifications based on the original video. Parts not mentioned remain unchanged by default.​

  * Applicable scenarios: local replacement, subject removal, attribute modification, etc.​

  * Recommended patterns:​

  * Add elements: Clearly describe <Element_Features> \+ <Timing> \+ <Location>​

  * Modify elements: Strictly edit <Video_N>, and modify <Original_Characteristic> in it to <New_Characteristic>​

  * Delete elements: Specify the elements that need to be deleted. For elements that should remain unchanged, emphasize them in the prompt for better performance.​

Video extension​

Continue the original video along the time dimension, requiring the audio-video style, subject, and narrative to remain consistent.​

  * Applicable scenarios: continuing the plot, extending actions, completing clips, etc.​

  * Recommended patterns:​

  * Extend video: Extend <Video_N> forward/backward to generate...​

  * Track completion: <Video_1> \+ <Transition_Description> \+ followed by <Video_2> \+ <Transition_Description> \+ followed by <Video_3>​

Note​

For edit / extend video tasks, directly use "<Video_N>" to refer to the video. Do not use "reference <Video_N>", to avoid being incorrectly identified as a reference task.​

Combined tasks​

The above three types of tasks can also be used in combination.​

  * Applicable scenarios: reference one asset and edit another asset.​

  * Recommended sentence patterns:​

  * Reference [Reference_Dimension] of <Image/Video_N>, strictly edit <Video_X>, [Specific_Edits]​

Advanced formula​

Seedance 2.0 is essentially a multimodal AI director: it reads your text prompts, images, videos, and audio simultaneously, and internally breaks them down into two dimensions, the "spatial layer" (what is in the frame) and the "temporal layer" (how things change over time), to understand and generate visuals.​

Therefore, a good prompt is not simply "copywriting-style description", but an "engineering-style instruction": who, in what scene, doing what action, how the camera moves, and in what chronological order events occur are delivered respectively to the spatial layer and the temporal layer. The specific formula is as follows:​

​

text

Copy

Advanced prompt formula: precise subject + action details + scene/environment + lighting & color tone + camera movement + visual style + image quality + constraints​

​

​​​

​​​

​​​

​​​

​

In simple terms, first lock in "who" is "doing what", then explain "where" and "what atmosphere", then tell the model "how to shoot", and finally tighten the result with style, image quality, and constraints. The following sections break down each element in detail.​

1\. Define the subject​

In the actual referenced asset, one image often contains multiple subjects. To precisely reference a specific object in the asset, you must clearly define the subject. The subject can be a person, prop, scene, etc.​

​

Basic Definition

Single Subject Across Multiple Materials

Multi-subject Scenario

​

  * Recommended pattern: Define [Core_Subject_Features] in <Image/Video_N> as <Subject_N>​

  * Core feature requirements: Use 2–3 clear and stable static features (such as clothing, hairstyle, appearance, or category) to describe the subject and ensure it can be uniquely identified.​

  * Examples:​

  * Define the woman wearing a red dress and a straw hat in Image 1 as Subject 1​

  * Define the woman wearing a red dress and a straw hat in Image 1 as Zhang Hong​

When objects in multiple assets refer to the same subject, bind them consistently:​

  * Recommended pattern: Define [...] in Image 1 and [...] in Image 2 as <Subject_N>​

When multiple subjects appear in a video, define them separately and distinguish them with labels. Labels must be unique and stable, and the corresponding labels must be used consistently in subsequent descriptions to avoid reference ambiguity.​

  * Recommended pattern: Define [Core_Features_Of_Subject_1] in <Image/Video_N> as <Subject_1>, and define [Core_Features_Of_Subject_2] in <Image/Video_N> as <Subject_2>...​

  * Example: Define the tall man in Video 1 as police officer, and define the other short man as thief. The scene is set in a crowded daytime market, with bright sunlight, many fruit stalls, and dense pedestrian traffic, creating a lively street-market atmosphere. Thief runs forward in panic through the crowded market, while police officer follows closely behind at full speed. The two quickly weave through the stalls. A handheld camera rapidly tracks forward, with slight realistic camera shake, creating a tense chase atmosphere.​

​

Note​

  * Each time a subject is involved, it must be explicitly referred to to avoid omission. The following two usages are supported:​

  * For simple scenarios with undefined subjects, each time the subject is mentioned, use <Subject_N>@<Image_N> to emphasize the binding relationship between the subject and the asset. For example: Zhang San@Image 1.​

  * For scenarios where subjects have been defined in advance, each time the subject is mentioned, the same label should be used. For example: define the tall man in Video 1 as police officer, and define the other short man as thief. In subsequent descriptions, when referring to the tall man, consistently use "police officer"; when referring to the short man, consistently use "thief".​

  * When using the asset library (Asset ID), you still need to use <Image/Video_N> to refer to the subject. Because the model cannot directly associate the Asset ID with the reference content, you must not directly use the Asset ID instead of <Image/Video_N>.​

  * Keep descriptions as concise as possible, avoid redundancy, and avoid semantic conflicts (such as contradictory characteristics for the same subject).​

  * It is recommended to express spatial relationships through reference images first, reducing complex text descriptions.​

2\. Shot sequencing​

The model's internal modeling decouples space and time. Therefore, the ideal prompt form for a complex video is a timeline-based storyboard: break the video into several shots, and dynamically describe each shot in the order events occur: who + where + doing what + how the camera moves.​

Suggestions​

Use shot order, write a simple "Shot 1 / Shot 2 / Shot 3" storyboard for each segment of the video, and then merge them into a complete prompt.​

  * Negative example: "A man runs nervously down the street, and the scene feels very cinematic."​

  * Positive example:​

  * Shot 1: Side shot of a street alley; the man slowly starts running, with a sense of rapid breathing.​

  * Shot 2: The man knocks over a fruit stand; the camera shakes quickly and gives a close-up of the man's frightened face.​

  * Shot 3: The man climbs over a low wall and disappears; the camera slowly pulls back and freezes on the empty street.​

Rules​

  * Use identifiers such as Shot 1, Shot 2, and Shot 3 to organize content in the order events occur (primary first, secondary later). Do not impose strict limits on the duration of each segment; prioritize allowing the model to naturally generate the pacing based on the plot.​

Tip​

The model's support for precise timing (such as 0–3 seconds) is unstable, and forcibly limiting duration may lead to abnormal generation results.​

  * It is recommended to organize each shot according to the following logic:​

  1. Camera movement or shot transition method: such as "slowly push in from a wide shot," "fixed camera position," "cut to..." and so on.​

  2. Subject actions and expressions: describe the key actions and changes in expression of the core character / object.​

  3. Position or spatial changes: explain the scene, position, or spatial relationship where the subject is located.​

  4. Audio information: describe the sound effects, voices, background music, etc. corresponding to the shot.​

3\. Action description requirements​

  * Body-movement refinement + degree quantification​

  * Actions should be specific to body parts such as hands, legs, head, shoulders, and back, while also supplementing descriptions of range, speed, and force;​

  * Examples: slowly raise a hand, quickly turn the head, push hard off the ground, slightly lower the head.​

  * Prioritize slow, gentle, continuous small movements​

  * Prioritize slow, gentle, coherent subtle movements, and try to avoid high-burst, large-dynamic actions such as sprinting, big jumps, and violent rolls.​

  * Examples: walk slowly, gently raise a hand, slightly lower the head, sit down naturally with the motion​

  * Supplement transitions between actions​

  * Specify the inertia and continuity between preceding and following actions to ensure the on-screen movement is coherent and natural.​

  * Examples: use the inertia of turning around to naturally raise a hand, naturally transition from a pause into raising a hand.​

  * Concrete external expression of emotions​

Use specific physical details to express emotions, replacing abstract words such as "very sad" and "extremely angry."​

See the table below for specific examples:​

​

Abstract emotion​| Externalized as actions and details​
---|---

Abstract emotion​| Externalized as actions and details​
---|---
Sadness​| lowering the head, shoulders trembling slightly, eyes reddening, fingers unconsciously clutching the corner of clothing, tears welling in the eyes but not falling​
Joy​| the corners of the mouth rising uncontrollably, brows and eyes relaxing, steps becoming light, unconsciously humming a tune, unable to resist spinning in place​
Nervousness / anxiety​| frequently checking the watch, fingers constantly tapping the tabletop, rapid breathing, eyes darting away, unconsciously biting fingernails​
Anger​| both fists clenched, jawline tense, chest heaving violently, eyes as sharp as knives, squeezing words out through gritted teeth​
Relief​| letting out a long breath, tense shoulders completely relaxing, a long-lost faint smile appearing on the face, looking up toward the distance​

​

4\. Camera movement prompts​

The model has a strong understanding of camera movement terms, so you can directly use standard camera movement terminology, such as "medium shot, close-up, wide shot, slow push-in, smooth lateral tracking, fixed shot." For more, see [Lens language](https://ai.byteplus.com/ark/region:ap-southeast-1/docs/seedance-1-0-pro-pro-fast#a395fd3b).​

Note​

Try to specify only 1 type of camera movement in a single shot. Do not require push, pull, pan, and move at the same time, as this will increase image instability.​

5\. Image quality, style and constraint words​

Image quality, style, and constraint words are key to controlling video generation results. They can define creative boundaries for the model, unify image quality and artistic tone, and avoid visual flaws and random deviations, making them necessary configurations for ensuring stable and compliant final output.​

1 Image quality​

Define image clarity, detailed textures, and lighting quality to improve the basic image quality of the final video.​

Examples: HD, rich details, cinematic texture, natural colors, soft lighting​

2 Style​

Set the overall art style and visual tone to unify the artistic atmosphere of the image.​

Examples: cyberpunk cool blue-purple tone, retro film, fresh Japanese style​

3 Constraint words​

Constraint words are very important. They can effectively avoid visual flaws, deformities, breakdowns, and unreasonable elements, and constrain the generation boundaries and stability.​

Common constraint word templates:​

  * Avoid generating subtitles: "keep it subtitle-free," "avoid generating any text or subtitles"​

  * Avoid generating a Logo: "do not generate a logo"​

  * Avoid generating a watermark: "do not generate a watermark"​

6\. Cases​

Demonstrate how to use the advanced formulas and elements introduced above to write prompts.​

​

Example 1: Dormitory emotional short drama (dialogue-focused)

Example 2: Ancient-style cliff confrontation (action/atmosphere-focused)

​

Asset preparation:​

  * @Image 1: Half-body photo of the female lead​

  * @Image 2: Dormitory scene reference image​

  * @Video 1: Camera movement reference for indoor dialogue (medium-shot dolly in/out or slight pan)​

  * @Audio 1: Indoor ambient sound or light music​

Prompt:​

Use the girl in @Image 1 as the main character, use @Image 2 as the dormitory scene style reference, and refer to the camera movement in @Video 1.​

Shot 1: At dusk, girl @Image 1 walks briskly to the dormitory entrance @Image 2. The camera follows steadily in a medium shot. Warm yellow sunlight spills into the hallway from the window. She pauses at the doorway, takes a deep breath, and looks slightly nervous.​

Shot 2: Girl @Image 1 pushes the door open and enters the dormitory. The camera cuts to an indoor medium shot. Her roommates look up at her while organizing their books. One of them smiles and asks {How did the exam go? Did you pass?}. The camera slowly cuts between half-body close-ups of several people.​

Shot 3: Girl @Image 1 first lowers her head with a dejected expression. The camera gives her a close-up. Then she raises her head, unable to hold back a smile, laughs out loud, and says {I was kidding}. Her roommates start chasing and play-fighting with her. The camera slowly pulls back and freezes on a wide shot of the dormitory filled with laughter.​

The entire video should have a high-definition cinematic documentary style, with warm tones and soft lighting. The character’s face remains stable without deformation; movements are natural and smooth, with no stutter or flicker. The ambient sound blends naturally with @Audio 1.​

Asset preparation:​

  * @Image 1: Female lead in red​

  * @Image 2: Assassin in black (opponent)​

  * @Image 3: Cliff and bamboo forest scene image​

  * @Video 1: Camera movement reference for martial arts confrontation​

  * @Audio 1: Tight drum beats or fight sound effects​

Prompt:​

Use the woman in red from @Image 1 as the female lead, use the woman in black from @Image 2 as the opponent, use the cliff and bamboo forest environment in @Image 3 as the scene reference, refer to the overall camera movement and action rhythm in @Video 1, and synchronize the background sound effects with @Audio 1.​

Shot 1: At dusk, the camera slowly pushes in from a side medium shot of woman in red @Image 1. She stands at the edge of the cliff and lifts a wine flask to drink. Her sleeves and robe hem sway gently in the mountain wind. The camera circles halfway around her, moving from the front to her back. In the distance, a figure in black is faintly visible in the bamboo forest.​

Shot 2: The camera zooms and fades into a long shot. From a drone perspective, it overlooks the entire cliff and bamboo forest. The two characters stand at opposite ends of the cliff. The mountain wind lifts their robe hems and dust, and the rhythm slightly accelerates with the drum beats.​

Shot 3: The camera cuts back to a ground-level close shot. The two slowly draw their swords and face off. Woman in red @Image 1 shifts from a careless expression to a cold gaze. Woman in black @Image 2 looks determined, and the sword tip trembles slightly. The camera steadily follows the two as they circle each other, finally freezing on a close-up of the instant before the two swords meet.​

The overall visual style should feel like a cinematic wuxia world in misty rain, with cool tones, low saturation, a film-grain texture, and rich light-and-shadow layers. The characters’ faces and body proportions remain stable without deformation. Movements are continuous and natural, not stiff, with no clipping or stutter.​

​

Other tips​

Text generation​

Seedance 2.0 series models support generating common text. The model can automatically match an appropriate style and color based on the context, and also supports specifying the color, style, appearance method, appearance timing, and appearance position of text in the prompt. When writing, please prioritize common characters and avoid rare characters and special symbols to ensure the best presentation. Currently, scenarios such as ad slogans, subtitles, and speech bubbles are supported. For specific writing methods and cases, see [Text generation](https://ai.byteplus.com/ark/region:ap-southeast-1/docs/seedance-2-0-prompt-guide#081b2c64).​

Video extension vs segmented stitching​

  * Continuous long take (video extension): suitable for "dialogue scenes" within a single scene, such as long conversations, emotional progression, and movement along a single path, to achieve an immersive and coherent one-shot effect.​

  * Scene / action turning points (segmented stitching): suitable for plot turns or complex, fast-paced "action scenes," such as chases, fights, montages, etc. Independent clips can be generated and then edited together to ensure rhythm and visual impact.​

In actual production, the two methods are usually combined. For example, first use extension to generate a coherent conversation, then stitch in empty shots or transition clips, balancing immersion with rhythmic variation.​

Asset configuration strategy​

Assets are usually divided into four "functional roles":​

  1. Character anchoring: lock the character appearance​

  2. Scene tone-setting: lock the environment and style​

  3. Camera movement reference: lock the shot language and action rhythm​

  4. Rhythmic atmosphere: use audio to control emotion and timbre​

Recommended configuration (4-5 assets in total): 1-2 character images (facial close-up / full body) + 1 scene image + 1 camera movement video + 1 audio clip.​

Tip​

It is not recommended to use the full asset limit. Too many assets will make it difficult for the model to judge feature priorities, which can easily cause issues such as style conflicts, blurry subject identification, and generated results deviating from expectations.​

Things to notice​

Language standards​

The language of dialogue must be consistent, and mixing Chinese and English should be avoided (except for proper nouns).​

Special character standards​

Reasonable use of symbols in prompts helps the model accurately understand different information types:​

​

Information type​| Symbol​| Example​
---|---|---

Information type​| Symbol​| Example​
---|---|---
Music​| ()​| (fast-paced rock music is playing in the background)​
Sound effect​| <>​| < dog barking can be heard in the distance >​
Dialogue​| {}​| {Hello, world}. If the dialogue is in a less common language (neither Chinese nor English), the language must be marked, such as: says in Japanese {こんにちは}.​
Subtitles​| []​| [Chapter One: Departure]​

​

FAQ​

Inaccurate face reference​

Typical symptoms​

The generated character appearance is inconsistent with the reference image, or "face swapping" occurs midway through the video (ID drift), causing the character in the video to resemble a celebrity and be blocked during review.​

Root Cause Analysis​

The face reference image is insufficiently effective​

  * Mixed reference images: Providing the model with a single combined image that includes the face reference, full-body/half-body pose reference, outfit reference, detail reference, and other reference elements.​

  * Face ratio is too small: In mixed reference images, the face area accounts for too small a proportion of the entire image. When extracting facial features, the model assigns insufficient weight to them and is easily disturbed by the background or other elements.​

Solution​

Strengthen the independence and weight of the face reference:​

  1. Prepare a close-up face image: In addition to the original full-body photo, prepare an extra close-up face image containing only the character's head (headshot, retaining only the face; no expression is best; minimize interfering elements such as shoulders, neck, and background).​

  2. Clearly define the subject in the prompt: <Subject 1> facial features reference image 1 (headshot), makeup and styling reference image 2 (full-body photo).​

  3. Place important assets first: The more an asset requires precise reference, the earlier it should be placed in the prompt.​

Note​

For character references, using a headshot + full-body photo is sufficient. Using multi-view character images is not recommended. Multi-view assets contain different angles of the same character, and the model may easily identify them as multiple different subjects, which instead worsens the ID drift issue.​

​

Before​| After​
---|---

Before​| After​
---|---
​ __ Replay Play 00:00 / 00:08 Live 00:00 Fullscreen Cssfullscreen 1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag ​​The character in the video "changes face" midway and resembles a celebrity​| ​ __ Replay Play 00:00 / 00:08 Live 00:00 Fullscreen Cssfullscreen 1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag ​​The face remains consistent with the reference image throughout​

​

Unexpected subtitles appear in the video​

Typical symptoms​

The prompt did not request subtitles, but the generated video contains subtitles.​

Solution​

Tip​

Currently, it is not possible to directly avoid generating subtitles 100%. You can only reduce the probability of their occurrence and improve the success rate through the following methods.​

  1. Add explicit constraint instructions to the prompt: "Keep it subtitle-free" and "Avoid generating any text or subtitles".​

  2. If the reference image or video contains text that is not essential, we recommend removing the text first using a tool, such as the image/video editing capabilities of Seedream or Seedance, and then using the text-free asset as input.​

  3. If your business allows, prioritize generating videos in landscape size (the probability of generating subtitles in landscape is significantly lower than in portrait). You can later crop it to portrait using editing software.​

Logo or watermark appears in the video​

Typical symptoms​

The prompt did not mention watermark-related content, but the generated video contains a Logo / watermark from another video platform.​

Solution​

Add explicit constraint instructions to the prompt: "Do not generate watermarks" and "Do not generate Logos".​

Style drifting​

Typical symptoms​

You expect to generate a 2D or 3D anime style, but the style of the input reference image is relatively realistic, and the prompt does not emphasize the video style. As a result, the generated video may drift into a live-action realistic style.​

Solution​

Add explicit style constraint words to the prompt, such as "2D Japanese anime style" or "3D Chinese-style comic". If more precise style control is required, it is recommended to first convert the reference image into the target style before generating the video.​

​

Before​| After​
---|---

Before​| After​
---|---
​ __ Replay Play 00:00 / 00:12 Live 00:00 Fullscreen Cssfullscreen 1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag ​​Xianxia style drifts into live-action style​| ​ __ Replay Play 00:00 / 00:12 Live 00:00 Fullscreen Cssfullscreen 1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag ​​Maintains the 3D Chinese animation CG xianxia style​

​

Jump cuts at video extension transition points​

Typical symptoms​

After using the video extension feature to generate a new video, when the new video is stitched with the original video, there may be frame jumps or rollback issues at the join.​

Solution​

The current recommendation is to repair this in post-editing by aligning keyframes. Fundamental optimization will be achieved through future model iterations.​

  1. Import the videos to be stitched into CapCut or other professional video editing software.​

  2. At the first join, trim 6 frames from the end of the previous video segment.​

  3. At the same time, trim 1 frame from the beginning of the following video segment.​

  4. Repeat the above operations for all stitching points.​

  5. Export and check the smoothness of the stitched video.​

Tip​

After video frame alignment, slight jumps may still exist. It is recommended to end the video when generating a prefill-based response video at the moment of a transition cut, and start the next video from the new scene after the ending cut.​

​

Before​| After​
---|---

Before​| After​
---|---
​ __ Replay Play 00:00 / 00:30 Live 00:00 Fullscreen Cssfullscreen 1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag ​​Instant screen jumps or content rollback occur at the transition points (5s, 20s)​| ​ __ Replay Play 00:00 / 00:30 Live 00:00 Fullscreen Cssfullscreen 1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag ​​The transitions are smoother​

​

Duplicated characters​

Typical symptoms​

In scenarios where there are many characters in the frame and three-view character images are provided as reference assets, two identical characters may easily appear in the same generated video frame.​

Root cause analysis​

  * The character subjects are not clearly defined in the prompt, so the model cannot accurately distinguish different character roles;​

  * When character three-view / multi-view images are used as reference assets, it is easy to confuse the model's character recognition, causing it to generate duplicate characters of the same appearance.​

Solution​

Tip​

Currently, it is not possible to directly avoid the twin problem 100%. The following methods can only reduce its probability and increase the success rate of generation attempts.​

  1. Clearly specify character-subject associations​

Clearly define each character role in the prompt and specify the correspondence between roles and reference images. It is recommended to mark the corresponding reference image after each character name and keep the format consistent.​

Example: Zhang San (corresponding to image 1) throws the green passbook toward Li Si (corresponding to image 2), who is standing.​

  2. Add global constraint instructions​

Add a fixed constraint at the end of the prompt: Throughout the video, characters with completely identical appearance, clothing, and accessories are prohibited. Do not generate duplicate avatars or a twin effect. Keep only a single corresponding character in the same frame, and do not reproduce repeated copies of characters.​

  3. Optimize reference assets​

For character reference images, prioritize independent single-person photos. Three-view or multi-view assets are not recommended.​

  4. Simplify and optimize the prompt​

Do not directly use the complete script as the prompt. Overly redundant copy can easily cause confusion in model understanding. Remove irrelevant descriptions and ensure the instructions are clear and focused.​

​

Before​| After​
---|---

Before​| After​
---|---
​ __ Replay Play 00:00 / 00:12 Live 00:00 Fullscreen Cssfullscreen 1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag ​​"Twins" appear at the 8th second of the video​| ​ __ Replay Play 00:00 / 00:12 Live 00:00 Fullscreen Cssfullscreen 1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag ​​

​

Image quality degradation during video extension​

Typical symptoms​

When a video generated by the model is used as an input asset for extension and continuation, image quality degradation occurs. Multiple continuations will compound the degradation, and mottled color blocks are especially likely to appear in character face regions.​

Solution​

Currently, the following methods can be used to mitigate image quality degradation. Fundamental optimization will be carried out later through model iterations:​

  1. Convert the original video into a white model video using Seedance 2.0, and then use it as the input asset for continuation.​

  * Reference prompt: Convert the video into a white 3D model. All characters should be unified as pure white 3D models, with no color, no texture, and no shadows; use a pure white background, stable structure, and smooth motion.​

  2. Prioritize high-definition images as reference assets.​

  3. Reasonably control the number of video continuations and avoid repeated stacked continuations.​

​

Before​| After​
---|---

Before​| After​
---|---
​ __ Replay Play 00:00 / 00:10 Live 00:00 Fullscreen Cssfullscreen 1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag ​​Directly continue based on the model output​| ​ __ Replay Play 00:00 / 00:11 Live 00:00 Fullscreen Cssfullscreen 1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag ​​Convert the model output into a white model video before performing continuation​

​

Special effects do not meet expectations​

Typical symptoms​

When a specific special effect is described through prompt text, the effect may not match expectations. For example, if the prompt specifies that the number "2999" appears with a countdown animation, the actually generated number scrolling effect may jump randomly and fail to follow standard countdown logic.​

Solutions​

It is recommended to use a reference video to define the special effect: input the target special-effect video into the model as a reference asset, so that the model can accurately understand the effect form and motion logic, and the generated result will better match expectations. For example: the way the number "2999" appears should reference video 1.​

​

Before​| After​
---|---

Before​| After​
---|---
​ __ Replay Play 00:00 / 00:10 Live 00:00 Fullscreen Cssfullscreen 1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag ​​The number scrolling effect has an obvious sense of disordered jumps​| ​ __ Replay Play 00:00 / 00:12 Live 00:00 Fullscreen Cssfullscreen 1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag ​​After adding the correct number scrolling effect video, the effect result meets expectations​​ __ Replay Play 00:00 / 00:02 Live 00:00 Fullscreen Cssfullscreen 1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag ​​Effect animation​

​

Too many reference characters​

Typical symptoms​

When the number of reference people exceeds 4, the stability of the model output decreases, and the generated video may have issues such as an incorrect number of people (for example, too few or too many characters) or duplicated characters.​

Solution​

Currently, this can be mitigated in the following ways. In the future, fundamental optimization will be carried out based on model iterations:​

  1. Generate images step by step: Group the people to ensure that the number of people in each generated image does not exceed 4. For example, 6 people can be divided into 2 groups of 3 people each, and images can be generated separately.​

  2. Generate video from images: Use the multiple grouped images generated in the first step as reference assets, then generate the final video.​

​

Before​| After​
---|---

Before​| After​
---|---
​ __ Replay Play 00:00 / 00:10 Live 00:00 Fullscreen Cssfullscreen 1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag ​​Input 8 reference characters, and the output video has 9 people​| ​ __ Replay Play 00:00 / 00:10 Live 00:00 Fullscreen Cssfullscreen 1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag ​​After generating 2 images from the 8 characters, use image-to-video​

​

Noise at the end of the video​

Typical symptoms​

When a video contains narration, abrupt clicking sounds and cut-off noise are likely to appear at the end of the video.​

Solution​

Regenerate the video, or use editing tools such as CapCut to apply audio fade-out processing to the ending audio track through the volume envelope, eliminating cut-off noise.​

Specific steps (using CapCut):​

  1. Import the generated video into CapCut.​

  2. Select the video track on the timeline and click Audio in the toolbar.​

  3. Select the Volume envelope function (in some versions, it is located in the Basic / Adjust menu), and select keyframes. At this point, a line representing the volume and keyframes will appear on the audio track.​

  4. Near the end of the video, drag the final volume keyframe down to 0 volume to form a downward slope.​

​​​

  5. Preview and confirm that the ending audio fades out naturally, without sudden cutoffs or noise.​

​

Before​| After​
---|---

Before​| After​
---|---
​ __ Replay Play 00:00 / 00:04 Live 00:00 Fullscreen Cssfullscreen 1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag ​​There is noise at the end​| ​ __ Replay Play 00:00 / 00:04 Live 00:00 Fullscreen Cssfullscreen 1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag ​​There is no noise at the end​

​

Inaccurate Chinese pronunciation​

Typical symptoms​

The model is prone to mispronouncing polyphonic characters, uncommon characters, and characters with similar shapes.​

Solution​

You can replace text that is easy to misread with commonly used homophones with the same pronunciation to avoid pronunciation deviations and restore the expected audio effect. Note that this solution is only an optimization method and cannot completely avoid all pronunciation issues.​

Example: You can rewrite "螭龙山" in the prompt as the homophone "吃龙山".​

​

Before​| After​
---|---

Before​| After​
---|---
​ __ Replay Play 00:00 / 00:09 Live 00:00 Fullscreen Cssfullscreen 1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag ​​The pronunciation of "螭" in "螭龙山" is incorrect​| ​ __ Replay Play 00:00 / 00:09 Live 00:00 Fullscreen Cssfullscreen 1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag ​​After changing it to "吃龙山", the pronunciation is correct​

​

Inaccurate voice reference​

Typical symptoms​

When using reference audio to specify a voice, the audio voice in the final generated video differs significantly from the reference voice.​

Solution​

  1. Add detailed descriptions of voice characteristics in the prompt. You can refer to the [Seedance-1.5-pro Prompt Guide](https://ai.byteplus.com/ark/region:ap-southeast-1/docs/seedance-1-5-pro).​

  2. Keep the style of the video lines close to the tone and expression style of the reference audio, which helps improve voice restoration and stability.​

​

Before​| After​
---|---

Before​| After​
---|---
​ __ Replay Play 00:00 / 00:05 Live 00:00 Fullscreen Cssfullscreen 1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag ​​The voice does not match the input audio​​​Audio.mp3​​Audio input​| ​ __ Replay Play 00:00 / 00:05 Live 00:00 Fullscreen Cssfullscreen 1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag ​​After adding descriptions of voice characteristics to the prompt, the voice matching accuracy improves significantly​"Use the low, thick, warm, and finely grainy middle-aged male voice of @Audio 1 to say"​

​

Appendix: Prompt examples​

This section shows prompt examples for using Seedance 2.0 series models in different scenarios, helping you more precisely implement functions such as referential control for omni references and text generation. For more excellent examples, refer to the [Seedance2.0](https://ai.byteplus.com/ark/region:ap-southeast-1/experience/gen_video?model=dreamina-seedance-2-0-260128) template library in the console.​

Text generation​

Slogans​

Prompt template:​

​

plaintext

Copy

[Text Content] + [Timing] + [Positioning] + [Entrance/Appearance Style], [Visual Attributes (Color, Font Style)]​

​

Tip​

Seedance2.0 can match an appropriate text style based on the context. If you have strict requirements for text presentation, refer to Multi-image reference > Logo below.​

Examples:​

[Output]​

​

__

Replay

Play

00:00 / 00:04 Live

00:00

Fullscreen

Cssfullscreen

1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag

​​

[Prompt]​

Hand-drawn comic style: Three people are sitting around a table enjoying the fried chicken shown in Image 1, with a friendly and joyful atmosphere. The frame then gradually blurs, and the text "Bite", "Laugh", and "Seedance" in order appears in the center of the screen.​

[Reference material]​

​​​

▲ Image 1​

​

Subtitles​

Prompt template:​

​

plaintext

Copy

Display subtitles at the bottom-center with the text. The subtitles must be perfectly synchronized with the audio rhythm and pacing.​

​

Examples:​

Voiceover​

​​

[Output]​

​

__

Replay

Play

00:00 / 00:11 Live

00:00

Fullscreen

Cssfullscreen

1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag

​​

[Reference material]​

​​​

▲ Image 1​

[Prompt]​

I2V: A time-lapse of a mountain landscape transitioning from a vast, starry night to a vibrant dawn. Voiceover: A deep, serene male voice says: 'In the vast silence of the cosmos, our world is but a fleeting moment. Yet, within it, life defiantly thrives.' > Text Integration: Render the narration as subtitles at the bottom-center. Subtitles must be perfectly synchronized with audio timing.​

Dubbing​

​​

[Output]​

​

__

Replay

Play

00:00 / 00:06 Live

00:00

Fullscreen

Cssfullscreen

1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag

​​

[Reference material]​

​​​

▲ Image 1​

[Prompt]​

R2V: A shot of these two people in Image 1 chatting in a modern office. The woman speaks first with a playful tone: "You always arrive right on time, don't you just love that perfect timing?" followed by the man's smiling reply: "I have my own rhythm." > Text Integration: Render the dialogue as subtitles at the bottom-center of the screen. Subtitles should appear sequentially as each character speaks.​

​

Speech bubbles​

Prompt template:​

​

plaintext

Copy

[Character] says, "[Dialogue]." Speech bubbles appear around the character containing the spoken text.​

​

Examples:​

[Output]​

​

__

Replay

Play

00:00 / 00:04 Live

00:00

Fullscreen

Cssfullscreen

1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag

​​

[Reference material]​

​​​

[Prompt]​

The two characters from Image 1, both dressed in sportswear, are running on the school playground. The girl looks at the boy, smiling confidently as she says: "We can definitely do it!". Cut to a close-up of the boy. He hesitates and replies: "Are you sure?". Cut back to a medium close-up of the girl. She speaks in a light, upbeat tone: "Yes!" Her demeanor is bright and resolute. Speech bubbles containing the corresponding lines appear around the speaking character.​

[Output]​

​

__

Replay

Play

00:00 / 00:05 Live

00:00

Fullscreen

Cssfullscreen

1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag

​​

[Reference material]​

​​​

[Prompt]​

Refer to the character design of the girl in Image 1 and Image 2. The scene is set in an apple field: the girl picks one apple, takes a bite, smiles and says "This is the real deal!". A speech bubble pops up beside the girl, with this line written inside.​

​

Image reference​

Seedance 2.0 series supports multi-perspective references for subjects, as well as multi-image referencing for scene layouts, sequences, and more.​

If your creative process requires a specific order (for example for sequential motion), please upload your images in the desired sequence. You can then use specific identifiers in your prompt for precise control: Refer to Image 1, Image 2, ..., Image N to accurately map each reference to your instructions.​

Multi-perspective subject reference​

Prompt template:​

​

plaintext

Copy

Refer to/Extract/Combine/Use the [Subject] from [Image N] to generate [Scene Description], maintaining consistent [Subject] features.​

​

Make sure that you identify the reference objects clearly. The model can process instructions including, but not limited to, the following examples.​

Products:​

Consumer electronics​

​​

[Output]​

​

__

Replay

Play

00:00 / 00:05 Live

00:00

Fullscreen

Cssfullscreen

1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag

​​

[Reference material]​

​​​

[Prompt]​

Use the cameras featured in Image 1, Image 2 and Image 3. Replace the original background with a white one, and place the cameras on a white table. The camera first focuses on the cameras in close-up, then slowly rotates 360° with the cameras as the main subject, clearly displaying the front, sides and back of each camera.​

Home & lifestyle​

​​

[Output]​

​

__

Replay

Play

00:00 / 00:06 Live

00:00

Fullscreen

Cssfullscreen

1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag

​​

[Reference material]​

​​​

[Prompt]​

In a warm-toned home setting, present the thermos shown in the reference image in a medium shot. Then smoothly push the camera into a close-up of the thermos. Next, a hand naturally enters the frame off-screen, gently grips the thermos body and picks it up. The camera follows the slight rotating motion of the hand to showcase the thermos.​

​

​​

Characters:​

[Output]​

​

__

Replay

Play

00:00 / 00:07 Live

00:00

Fullscreen

Cssfullscreen

1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag

​​

[Reference material]​

​​​

[Prompt]​

Refer to the image of the woman in Image 1, Image 2 and Image 3, and generate a scene of her eating a cake in a coffee shop.​

​

Multi-image reference​

Prompt template:​

​

plaintext

Copy

Refer to / Extract / Combine / Follow the [Description of referenced elements] from [Image N] to generate [Scene Description], while maintaining the consistency of [Referenced Elements].​

​

Examples:​

Logo reference​

​​

[Output]​

​

__

Replay

Play

00:00 / 00:10 Live

00:00

Fullscreen

Cssfullscreen

1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag

​​

[Reference material]​

​​​

[Prompt]​

The scene is set on an aerial corridor in a neon-drenched futuristic metropolis, where flying vehicles and holographic ads intertwine. Featuring the girl from Reference Image 2, the sequence opens with a medium shot of her releasing a silver floating lantern embedded with a holographic projection. The camera then pulls back to reveal floating lanterns flooding the sky, which gradually converge at the center of the frame to form the logo from Reference Image 1. The entire piece adopts a 3D cyberpunk sci-fi animation style.​

Multi-subject reference​

​​

[Output]​

​

__

Replay

Play

00:00 / 00:11 Live

00:00

Fullscreen

Cssfullscreen

1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag

​​

[Reference material]​

​​​

[Prompt]​

Using the cat and dog from the reference Image 1 and Image 2 as prototypes, the scene unfolds in a cozy apartment. The dog is lying on the ground eating dog food when the cat approaches, extending a paw to nudge the dog. The dog pauses its meal upon noticing the cat, and the cat snuggles up next to the dog. The entire scene features a warm colored tone.​

​

Multi-element reference​

​​

[Output]​

​

__

Replay

Play

00:00 / 00:15 Live

00:00

Fullscreen

Cssfullscreen

1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag

​​

[Reference materials]​

​​​

[Prompt]​

The scene is set in the restaurant from image 4 with people coming and going. The girl from image 1, wearing the clothes from image 2, is organizing the items on the counter. The boy, a customer, from image 3 approaches her to ask for her contact information. The logo from image 5 remains in the bottom right corner throughout.​

​

Multi-panel sequence reference​

​​

[Output]​

​

__

Replay

Play

00:00 / 00:14 Live

00:00

Fullscreen

Cssfullscreen

1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag

​​

[Reference materials]​

​​​

▲ Image 1​

[Prompt]​

Refer to the sequence in Image 1 to create an intense high-energy fight sequence. All frame compositions from Image 1 shall be presented in strict predefined order, after which the two characters engage in fierce, fast-paced combat.​

Sequence Reference​

​​

[Output]​

​

__

Replay

Play

00:00 / 00:15 Live

00:00

Fullscreen

Cssfullscreen

1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag

​​

[Reference material]​

​​​

[Prompt]​

Refer to the composition in Image 3. A girl (her character design refers to Image 1) is waiting for her father to finish cooking, and she says: "아빠, 배고파요! 밥 다 됐어요?" Then the camera pans right and cuts to the frame and composition shown in Image 4. The father (his character design refers to Image 2) replies to her: "거의 다 됐어, 조금만 기다려!" Next, the camera cuts back to a close-up shot of the daughter's slightly disappointed facial expression, and she says: "아직 멀었어요? 맛있는 냄새 나는데..." Then the shot switches to a close-up of the father's face, and he says: "이제 진짜 금방이야. '빨리빨리' 하지 말고 손부터 씻고 와!"​

​

Video reference​

Seedance 2.0 series supports video-based referencing.​

  * If your workflow requires a specific sequence, please upload the files in order. You can use Video 1, Video 2, ..., Video N in your prompts for precise mapping.​

  * Simply ensure that the relationship between the generated content and the reference source is clearly defined.​

Motion reference​

Prompt template:​

​

plaintext

Copy

Refer to the [Motion Description] from [Video N] to generate [Scene Description], keeping the motion details consistent.​

​

Examples:​

Artistic​

​​

[Output]​

​

__

Replay

Play

00:00 / 00:05 Live

00:00

Fullscreen

Cssfullscreen

1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag

​​

[Reference materials]​

​

__

Replay

Play

00:00 / 00:05 Live

00:00

Fullscreen

Cssfullscreen

1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag

​​

▲ Video 1​

​​​

[Prompt]​

Refer to the character movements and shot language in Video 1 to create a fight scene with the character from Image 2 on the left and the character from Image 1 on the right. Include intense background music.​

Marketing​

​​

[Output]​

​

__

Replay

Play

00:00 / 00:05 Live

00:00

Fullscreen

Cssfullscreen

1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag

​​

[Reference materials]​

​

__

Replay

Play

00:00 / 00:12 Live

00:00

Fullscreen

Cssfullscreen

1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag

​​

▲ Video 1​

[Prompt]​

Referencing the running shape of the horse in the video, generate a scene: a golden steed runs on the grassland, then freezes its magnificent running posture and turns into a horse-shaped gold pendant.​

​

Camera motion reference​

Prompt template:​

​

plaintext

Copy

Refer to the [Camera Movement Description] from [Video N] to generate [Scene Description], keeping the scene consistent.​

​

Examples:​

[Output]​

​

__

Replay

Play

00:00 / 00:08 Live

00:00

Fullscreen

Cssfullscreen

1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag

​​

[Prompt]​

Referring to the camera movement in video 1, create a concept video for a science and technology park, with the tall building in the image as the visual center, also using a first-person diving perspective, to reflect the sense of technology in the park from image 1.​

[Reference material]​

​

__

Replay

Play

00:00 / 00:06 Live

00:00

Fullscreen

Cssfullscreen

1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag

​​

▲ Video 1​

​​​

▲ Image 1​

​

Special effects reference​

Prompt template:​

​

plaintext

Copy

Refer to the [Special effects description] from [Video N] to generate [Scene description], keeping the special effects consistent.​

​

Examples:​

Film​

​​

[Output]​

​

__

Replay

Play

00:00 / 00:08 Live

00:00

Fullscreen

Cssfullscreen

1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag

​​

[Reference material]​

​

__

Replay

Play

00:00 / 00:08 Live

00:00

Fullscreen

Cssfullscreen

1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag

​​

▲ Video 1​

​​​

▲ Image 1​

[Prompt]​

Refer to the golden particle effects in Video 1, so that when the character in Image 1 plays the flute, the same particle effects surround their body.​

Creative effects​

​​

[Output]​

​

__

Replay

Play

00:00 / 00:08 Live

00:00

Fullscreen

Cssfullscreen

1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag

​​

[Reference material]​

​

__

Replay

Play

00:00 / 00:12 Live

00:00

Fullscreen

Cssfullscreen

1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag

​​

▲ Video 1​

​​​

▲ Image 1​

[Prompt]​

Refer to the special effects shown in Video 1 to generate identical wings for the girl in Image 1, ensuring the wing formation trajectory follows the exact same motion path and sequence depicted in the video.​

​

Video editing​

Seedance 2.0 series supports video editing, including adding, removing, or modifying elements, extending the video duration (forward and backward), and track alignment.​

If your project requires a specific sequence, please upload the files in order. You can use Video 1, Video 2, ..., Video N in your prompts for precise mapping.​

Adding, removing, or modifying elements​

Prompt template:​

​

plaintext

Copy

Adding: At [Timestamp/Timing] and [Spatial Location] of [Video N], add [Description of intended element].​

Removing: Remove [Element to be deleted] from [Video N], keeping the rest of the video content unchanged.​

Modifying: Replace [Description of element to be changed] in [Video N] with [Description of intended element].​

​

Examples:​

Add elements​

​​

[Output]​

​

__

Replay

Play

00:00 / 00:08 Live

00:00

Fullscreen

Cssfullscreen

1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag

​​

[Reference material]​

​

__

Replay

Play

00:00 / 00:08 Live

00:00

Fullscreen

Cssfullscreen

1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag

​​

▲ Video 1​

[Prompt]​

Add snacks such as fried chicken and pizza to the countertop in Video 1.​

Remove elements​

​​

[Output]​

​

__

Replay

Play

00:00 / 00:11 Live

00:00

Fullscreen

Cssfullscreen

1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag

​​

[Reference material]​

​

__

Replay

Play

00:00 / 00:11 Live

00:00

Fullscreen

Cssfullscreen

1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag

​​

▲ Video 1​

[Prompt]​

Remove everything that isn't office supplies from the table in Video 1, keeping the rest of the video content unchanged.​

Modify elements​

​​

[Output]​

​

__

Replay

Play

00:00 / 00:06 Live

00:00

Fullscreen

Cssfullscreen

1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag

​​

[Reference material]​

​

__

Replay

Play

00:00 / 00:06 Live

00:00

Fullscreen

Cssfullscreen

1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag

​​

▲ Video 1​

​​​

▲ Image 1​

[Prompt]​

Replace the perfume featured in Video 1 with the face cream from Image 1, with all original motions and camera work preserved.​

​

Extending videos​

Prompt template:​

​

plaintext

Copy

\- Extend [Video N] forward/backward + [Description of extended content]​

\- Generate content before/after [Video N] + [Description of extended content]​

​

Note​

The model will automatically extract the transition frames for seamless blending. The original segments of the input video will not be re-generated, ensuring perfect continuity.​

Examples:​

Extend forward​

​​

[Output]​

​

__

Replay

Play

00:00 / 00:13 Live

00:00

Fullscreen

Cssfullscreen

1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag

​​

[Reference material]​

​

__

Replay

Play

00:00 / 00:12 Live

00:00

Fullscreen

Cssfullscreen

1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag

​​

▲ Video 1​

[Prompt]​

Generate the content after Video 1: the two men who are late run towards them, the five people finally meet and have a friendly chat.​

Extend backward​

​​

[Output]​

​

__

Replay

Play

00:00 / 00:07 Live

00:00

Fullscreen

Cssfullscreen

1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag

​​

[Reference material]​

​

__

Replay

Play

00:00 / 00:06 Live

00:00

Fullscreen

Cssfullscreen

1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag

​​

▲ Video 1​

[Prompt]​

Extend the opening segment of Video 1: Set up an over-the-shoulder shot of the man in a hoodie, and the man says: "It's not that bad. You're just stressed. Everyone goes through this, you just need to keep going."​

​

Completing tracks​

Prompt template:​

​

plaintext

Copy

[Video 1] + [Transition Description] + followed by [Video 2] + [Transition Description] + followed by [Video 3]​

​

Tip​

Input Limit: Seedance 2.0 series supports a maximum of 3 video clips as input. The total combined duration must not exceed 15 seconds.​

Smart Trimming: During generation, the model will automatically trim the connecting segments of the start and end clips, retaining only the necessary frames to ensure a seamless and logical synthesis.​

Examples:​

[Output]​

​

__

Replay

Play

00:00 / 00:12 Live

00:00

Fullscreen

Cssfullscreen

1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag

​​

[Prompt]​

Video 1. The moment a leaf falls to the ground, it sets off a special effect of golden particles. A gust of wind blows by, leading into Video 2.​

[Reference material]​

​

__

Replay

Play

00:00 / 00:04 Live

00:00

Fullscreen

Cssfullscreen

1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag

​​

▲ Video 1​

​

__

Replay

Play

00:00 / 00:04 Live

00:00

Fullscreen

Cssfullscreen

1x

  * 2x
  * 1.5x
  * 1x
  * 0.75x
  * 0.5x

Click and hold to drag

​​

▲ Video 2​

​

​

Last updated:  November 7, 2026 05:10:38

Was this page helpful to you?

Yes

Yes

No

No

[Previous documentation：Dreamina Seedance 2.0 series tutorial](/en/docs/ModelArk/seedance-2-0)[Video generation tutorialNext documentation](/en/docs/ModelArk/video-generation-tutorial)

Highlight to feedback

Select the content you can quickly feedback the problem, and we will follow up

Don’t show me again

Ok, got it

Feedback
