#include "CoreMinimal.h"
#include "Modules/ModuleManager.h"
#include "Modules/ModuleInterface.h"
#include "EJAIDirectorSubsystem.h"

class FEJAIModule : public IModuleInterface
{
public:
	virtual void StartupModule() override
	{
		UE_LOG(LogTemp, Warning, TEXT("[EJAI] Nelson Director Subsystem Initialized. Ready for action."));
	}

	virtual void ShutdownModule() override
	{
		UE_LOG(LogTemp, Warning, TEXT("[EJAI] Nelson Director Subsystem Shutdown."));
	}
};

IMPLEMENT_MODULE(FEJAIModule, EJAI);
