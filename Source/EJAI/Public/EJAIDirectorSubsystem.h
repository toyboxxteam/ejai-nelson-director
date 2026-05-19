#pragma once

#include "CoreMinimal.h"
#include "EditorSubsystem.h"
#include "EJAIDirectorSubsystem.generated.h"

// The Checkmark Protocol
USTRUCT(BlueprintType)
struct FEJAITaskStep
{
	GENERATED_BODY()

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category="EJAI")
	FString TaskName;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category="EJAI")
	bool bIsComplete = false;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category="EJAI")
	float Progress = 0.0f; // For the animation circle
};

UCLASS()
class EJAI_API UEJAIDirectorSubsystem : public UEditorSubsystem
{
	GENERATED_BODY()

public:
	// Nelsons Persona Prompt - The Master Instruction
	static const FString NelsonPersonaPrompt;

	// Starts the "Double Team" logic (GTA SA Style)
	UFUNCTION(BlueprintCallable, Category="EJAI | Nelson")
	void StartNelsonOrchestration(FString UserRequest);

	// Execution Manifest Logic
	UPROPERTY(BlueprintReadOnly, Category="EJAI | Nelson")
	TArray<FEJAITaskStep> CurrentManifest;

	// BettaHuman: 2D to 3D Harvester
	UFUNCTION(BlueprintCallable, Category="EJAI | BettaHuman")
	void HarvestFaceToMesh(UTexture2D* FaceTexture);

	// Get Nelson's current status
	UFUNCTION(BlueprintCallable, Category="EJAI | Nelson")
	FString GetNelsonStatus() const;

private:
	void AdvanceManifest(); // Step-by-step 1-2-3-4 logic
};
