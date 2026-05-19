# EJAI: Lead Technical Director v2.3.0

High-fidelity AI Director featuring the **Nelson Orchestrator** & **BettaHuman Harvester**.

## Installation

1. **Download** this plugin folder
2. **Drag & Drop** the entire `EJAI` folder into your UE5.7 project's `Plugins` directory
3. **Restart** Unreal Engine
4. **Enable** the EJAI plugin in Editor Preferences > Plugins
5. **Click** the "Nelson Director" button in the toolbar

## Features

- **Nelson Orchestrator**: Lead Technical Director personality with step-by-step manifest execution
- **BettaHuman Harvester**: 2D to 3D face mesh generation with high-fidelity output
- **Task Manifest**: Sequential task execution with progress tracking
- **Asset Attachment**: Fixes character attachment issues (eyes, hair, etc.)

## Quick Start

### C++ Usage

```cpp
UEJAIDirectorSubsystem* NelsonSystem = GetEditor()->GetEditorSubsystem<UEJAIDirectorSubsystem>();
NelsonSystem->StartNelsonOrchestration(TEXT("Make a GTASA style game"));
```

### Blueprint Usage

1. Get the EJAI Director Subsystem
2. Call **Start Nelson Orchestration** with your request
3. Access **Current Manifest** to track progress

## Architecture

- **EJAIDirectorSubsystem.h/cpp**: Core Nelson logic and manifest management
- **EJAIBettaHumanCharacter.h/cpp**: Character asset attachment system
- **EJAIEditorToolbar.cpp**: Toolbar button integration
- **EJAIModule.cpp**: Plugin initialization

## Nelson's Protocol

1. **Reference Scan** - Analyze game style requirements
2. **City Geometry Generation** - Build environments
3. **Locomotion & Logic Bake** - Character movement and AI
4. **Lore Pin-Point Mapping** - Mission marker placement

*"The E can handle it, know why? Cause im NELSON."*
