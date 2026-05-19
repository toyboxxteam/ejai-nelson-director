using UnrealBuildTool;

public class EJAI : ModuleRules
{
	public EJAI(ReadOnlyTargetRules Target) : base(Target)
	{
		PCHUsage = ModuleRules.PCHUsageMode.UseExplicitOrSharedPCHs;

		PublicDependencyModuleNames.AddRange(new string[] { 
			"Core", "CoreUObject", "Engine", "InputCore", "Projects", "AssetRegistry" 
		});

		PrivateDependencyModuleNames.AddRange(new string[] {
			"Slate", "SlateCore", "EditorStyle", "LevelEditor", "ToolMenus", "UnrealEd", "EditorSubsystem"
		});
	}
}
