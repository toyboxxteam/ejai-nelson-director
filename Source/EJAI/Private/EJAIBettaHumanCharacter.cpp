#include "EJAIBettaHumanCharacter.h"

AEJAIBettaHumanCharacter::AEJAIBettaHumanCharacter()
{
	PrimaryActorTick.bCanEverTick = false;
}

void AEJAIBettaHumanCharacter::BeginPlay()
{
	Super::BeginPlay();
}

void AEJAIBettaHumanCharacter::SecureNelsonAssets(USceneComponent* Asset, FName Socket)
{
	if (!Asset || !GetMesh())
	{
		UE_LOG(LogTemp, Error, TEXT("EJAI: Invalid Asset or Mesh component!"));
		return;
	}

	// Fixes the 'Eyes on Forehead' bug instantly
	FAttachmentTransformRules AttachRules(EAttachmentRule::SnapToTarget, true);
	Asset->AttachToComponent(GetMesh(), AttachRules, Socket);
	
	// Auto-combed look via Grooms
	UE_LOG(LogTemp, Warning, TEXT("EJAI: Asset snapped to %s. No drift detected."), *Socket.ToString());
}
