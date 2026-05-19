#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Character.h"
#include "EJAIBettaHumanCharacter.generated.h"

UCLASS()
class EJAI_API AEJAIBettaHumanCharacter : public ACharacter
{
	GENERATED_BODY()

public:
	AEJAIBettaHumanCharacter();

	virtual void BeginPlay() override;

	// Fixes the 'Eyes on Forehead' bug instantly
	UFUNCTION(BlueprintCallable, Category="EJAI | BettaHuman")
	void SecureNelsonAssets(USceneComponent* Asset, FName Socket);
};
