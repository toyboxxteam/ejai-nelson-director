#pragma once

#include "CoreMinimal.h"
#include "Widgets/DeclarativeSyntaxSupport.h"
#include "Framework/MultiBox/MultiBoxExtender.h"

class FEJAIEditorToolbar
{
public:
	static void RegisterToolbar();
	static void UnregisterToolbar();

private:
	static FSlateIcon GetToolbarIcon();
	static void OnNelsonToolbarButtonClicked();

	static TSharedPtr<FUICommandList> PluginCommands;
};
