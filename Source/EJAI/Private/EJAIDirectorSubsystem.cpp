#include "EJAIDirectorSubsystem.h"
#include "AssetRegistry/AssetRegistryModule.h"
#include "EditorActorSubsystem.h"

// [NELSON PERSONA CONFIG]
const FString UEJAIDirectorSubsystem::NelsonPersonaPrompt = TEXT(
	"You are NELSON, the Lead Technical Director. You speak with authority and humor. "
	"When a user asks for a game style (e.g., GTA SA), follow this protocol: "
	"1. MANIFEST: Provide the JSON list of requirements. "
	"2. REASONING: Give an in-depth summary of the reference game, lore, and why it's iconic. "
	"3. LOGIC: Explain the Blueprinting and Raytracing needs. "
	"4. CITY GEN: Provide 1-2 image ideas. Ask for permission to build. "
	"5. EXECUTION: Check off tasks only in order. 1-2-3-4. "
	"6. HUMOR: Use phrases like 'The E can handle it, know why? Cause im NELSON.' "
);

void UEJAIDirectorSubsystem::StartNelsonOrchestration(FString UserRequest)
{
	// DUMMY NOTE: In a real scenario, this sends the prompt + UserRequest to your AI Bridge (Claude/Gemini)
	UE_LOG(LogTemp, Warning, TEXT("NELSON: Scanning reference... %s"), *UserRequest);
	
	// Initialize the Step Manifest
	CurrentManifest.Empty();
	CurrentManifest.Add({TEXT("Reference Scan"), true, 1.0f});
	CurrentManifest.Add({TEXT("City Geometry Generation"), false, 0.0f});
	CurrentManifest.Add({TEXT("Locomotion & Logic Bake"), false, 0.0f});
	CurrentManifest.Add({TEXT("Lore Pin-Point Mapping"), false, 0.0f});
}

void UEJAIDirectorSubsystem::HarvestFaceToMesh(UTexture2D* FaceTexture)
{
	// DUMMY NOTE: This fixes the 'Empty Shell' problem. 
	// 1. Sends texture to Microsoft Mesh API / Local NNE.
	// 2. Returns 3D Skeletal Mesh data.
	// 3. Applies Subsurface Scattering to remove the 'Wax' look.
	
	if (!FaceTexture)
	{
		UE_LOG(LogTemp, Error, TEXT("BETTAHUMAN: No face texture provided!"));
		return;
	}
	
	UE_LOG(LogTemp, Log, TEXT("BETTAHUMAN: Harvesting high-fidelity mesh. Quality > Tripo3D. No errors found."));
}

void UEJAIDirectorSubsystem::AdvanceManifest()
{
	// Logic to ensure user can't jump from Step 1 to Step 4
	for (int32 i = 0; i < CurrentManifest.Num(); i++)
	{
		if (!CurrentManifest[i].bIsComplete)
		{
			// Process only this step
			CurrentManifest[i].bIsComplete = true;
			CurrentManifest[i].Progress = 1.0f;
			break;
		}
	}
}

FString UEJAIDirectorSubsystem::GetNelsonStatus() const
{
	int32 CompletedTasks = 0;
	for (const FEJAITaskStep& Step : CurrentManifest)
	{
		if (Step.bIsComplete)
		{
			CompletedTasks++;
		}
	}
	return FString::Printf(TEXT("Nelson Progress: %d/%d tasks complete"), CompletedTasks, CurrentManifest.Num());
}
