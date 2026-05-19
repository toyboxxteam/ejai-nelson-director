#include "EJAIEditorToolbar.h"
#include "LevelEditor.h"
#include "ToolMenus.h"

TSharedPtr<FUICommandList> FEJAIEditorToolbar::PluginCommands = nullptr;

void FEJAIEditorToolbar::RegisterToolbar()
{
	FLevelEditorModule& LevelEditorModule = FModuleManager::LoadModuleChecked<FLevelEditorModule>("LevelEditor");

	TSharedPtr<FExtender> Extender = MakeShareable(new FExtender());

	Extender->AddToolBarExtension(
		"Play",
		EExtensionHook::After,
		nullptr,
		FToolBarExtensionDelegate::CreateLambda([](FToolBarBuilder& ToolbarBuilder)
		{
			ToolbarBuilder.AddToolBarButton(
				FUIAction(FExecuteAction::CreateStatic(&FEJAIEditorToolbar::OnNelsonToolbarButtonClicked)),
				NAME_None,
				FText::FromString(TEXT("Nelson Director")),
				FText::FromString(TEXT("Launch EJAI Nelson Director")),
				GetToolbarIcon(),
				EUserInterfaceActionType::Button
			);
		})
	);

	LevelEditorModule.GetToolBarExtensibilityManager()->AddExtender(Extender);
}

void FEJAIEditorToolbar::UnregisterToolbar()
{
	UE_LOG(LogTemp, Warning, TEXT("[EJAI] Toolbar unregistered."));
}

FSlateIcon FEJAIEditorToolbar::GetToolbarIcon()
{
	return FSlateIcon(FAppStyle::GetAppStyleSetName(), "MainFrame.About");
}

void FEJAIEditorToolbar::OnNelsonToolbarButtonClicked()
{
	UE_LOG(LogTemp, Warning, TEXT("[NELSON] Double Team Protocol Activated. The E can handle it, know why? Cause im NELSON."));
}
