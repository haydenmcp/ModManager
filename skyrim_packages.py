from modcore import ModPackage
import skyrim_mods

class SkyrimModPackage(ModPackage):
    pass

class FoundationPatchPack(SkyrimModPackage):
    def mods(self):
        return (
            skyrim_mods.UnofficialHighResolutionPatch.Instance(),
            skyrim_mods.UnofficialSkyrimPatch.Instance(),
            # skyrim_mods.UnofficialSkyrimLegendaryEditionPatch.Instance(),
            skyrim_mods.OptimizedVanillaTextures.Instance(),
            skyrim_mods.StaticMeshImprovementMod.Instance(),
            skyrim_mods.SkyUI5.Instance(),
        )

class RealisticWorldWithRealVisionENB(SkyrimModPackage):

    # todo; remove environmental enhancements from high res pack. Enhancements should be separate.
    def mods(self):
        return (
            skyrim_mods.RuinsClutterImproved.Instance(),
            skyrim_mods.AlternateStart.Instance(),
            skyrim_mods.CinematicFireEffects.Instance(),
            skyrim_mods.HDEnhancedTerrain.Instance(),
            skyrim_mods.SkyrimDistanceOverhaul.Instance(),
            skyrim_mods.SkyrimDistanceOverhaulSkymillsPatch.Instance(),
            skyrim_mods.AnimatedDistantWaterfallsAndWindmills.Instance(),
            skyrim_mods.SkyrimHDFullVersion.Instance(),
            # skyrim_mods.SkyrimCityBeautificationAllInOneByJK.Instance(),
            skyrim_mods.VividLandscapesDungeonsAndRuins.Instance(),
            skyrim_mods.VividLandscapesDungeonsAndRuinsSMIMPatch.Instance(),
            skyrim_mods.VividLandscapesVolcanicArea.Instance(),
            skyrim_mods.AMidianBornCavesAndMines2k.Instance(),
            skyrim_mods.ImmersiveRoads.Instance(),
            skyrim_mods.ImmersiveRoadsReduceSnowShineTo40Percent.Instance(),
            skyrim_mods.SkyrimFloraOverhaul.Instance(),
            skyrim_mods.SkyrimFloraOverhaulTallPines.Instance(),
            skyrim_mods.TreesHD.Instance(),
            skyrim_mods.SimplyBiggerTrees.Instance(),
            skyrim_mods.SimplyBiggerTreesSlowerBranches.Instance(),
            skyrim_mods.ParallaxTreebark4K.Instance(),
            skyrim_mods.ParallaxTreebark4KSimplyBiggerTreesPatch.Instance(),
            skyrim_mods.ImmersiveFallenTrees.Instance(),
            skyrim_mods.FencesOfSkyrim.Instance(),
            skyrim_mods.RusticWindows2K.Instance(),
            skyrim_mods.VerdantGrassPlugin.Instance(),
            skyrim_mods.VerdantGrassPluginDarkGrassTextureOption.Instance(),
            skyrim_mods.NaturalGrassTextureFloor.Instance(),
            skyrim_mods.RealVisionFloraPatch.Instance(),
            skyrim_mods.HighDefinitionIvy2K.Instance(),
            skyrim_mods.DetailedRugs.Instance(),
            skyrim_mods.PureWatersLegendaryEdition.Instance(),
            skyrim_mods.PureWatersLandscapeTextures.Instance(),
            skyrim_mods.VividLandscapesRockingStonesParallax.Instance(),
            skyrim_mods.VividLandscapesCliffsAndCreeks.Instance(),
            skyrim_mods.VividLandscapesRockingStonesCompatibilityPatch.Instance(),
            skyrim_mods.VividLandscapesTundraMossRevisited.Instance(),
            skyrim_mods.VividLandscapesTundraSMIMPatch.Instance(),
            skyrim_mods.VividLandscapesTundraMossMountainPatch.Instance(),
            skyrim_mods.FinerDust.Instance(),
            skyrim_mods.RealisticSmokeAndEmbers.Instance(),
            skyrim_mods.LanternsOfSkyrim.Instance(),
            skyrim_mods.ParticlePatchForENB.Instance(), # todo: how to include ENB outside of this pack? It's not really related
            skyrim_mods.SubsurfaceScatteringPatchForENB.Instance(),
            skyrim_mods.ParallaxTerrain4K.Instance(),
            skyrim_mods.CoastBeachTexturesForParallax.Instance(),
            skyrim_mods.PineForestTexturesForParallax.Instance(),
            skyrim_mods.ClimatesOfTamriel.Instance(),
            skyrim_mods.ClimatesOfTamrielSupremeStorms.Instance(),
            skyrim_mods.ClimatesOfTamrielWeatherPatch.Instance(),
            skyrim_mods.TrueStorms.Instance(),
            skyrim_mods.RealisticLightingOverhaul.Instance(),
            skyrim_mods.EnbSeriesV308.Instance(),
            skyrim_mods.RealVisionENB.Instance(),
            skyrim_mods.RealVisionFloraPatch.Instance(),
            skyrim_mods.ShowRaceMenuPrecacheKiller.Instance(),
            skyrim_mods.XeniusCharacterEnhancementFull.Instance(),
            skyrim_mods.ApachiiSkyHairFull.Instance(),
            skyrim_mods.ApachiiSkyHairFemale.Instance(),
            skyrim_mods.ApachiiSkyHairMale.Instance(),
            skyrim_mods.ApachiiSkyHairNaturalRetexture.Instance(),
            skyrim_mods.DimonizedUNPFemaleBody.Instance(),
            skyrim_mods.AllInOneFacePackUNP.Instance(),
            skyrim_mods.BetterMalesFace.Instance(),
            skyrim_mods.BetterMalesBody.Instance(),
            skyrim_mods.EyesOfBeauty.Instance(),
            skyrim_mods.EyesOfBeautyNPC.Instance(),
            skyrim_mods.HighDefinitionTeeth.Instance(),
            skyrim_mods.RealisticRagdollsAndForce.Instance(),
        )

class HarshSkyrimImmersionPack(SkyrimModPackage):
    def mods(self):
        return (
            skyrim_mods.InterestingNPCs.Instance(),
            skyrim_mods.WetAndColdRegularEdition.Instance(),
            skyrim_mods.WetAndColdAshes.Instance(),
            skyrim_mods.CompleteCampingSystem.Instance(),
            skyrim_mods.Tentapalooza.Instance(),
            skyrim_mods.FrostfallSurvival.Instance(),
            skyrim_mods.RealisticNeedsAndDiseases.Instance(),
            skyrim_mods.ImmersivePatrols.Instance(),
            skyrim_mods.TouringCarriages.Instance(),
        )

    # TODO: Order of mods here is important. Make sure to update such that incompatibility,
    # TODO: dependencies, etc are intelligently resolved by application (order shouldn't matter
    # TODO: and should be dynamically resolved.

    # TODO: Resolve case when certain mod files cannot/need to overwrite other mod files.

    # TODO: Add SKSE Install potion?
    # Pass 1
    # mods = [
    #     skyrim_mods.SkyUI5(),
    #     skyrim_mods.UnofficialHighResolutionPatch(),
    #     skyrim_mods.UnofficialSkyrimPatch(),
    #     # skyrim_mods.UnofficialSkyrimLegendaryEditionPatch(),
    #     skyrim_mods.OptimizedVanillaTextures(),
    #     skyrim_mods.StaticMeshImprovementMod(),
    #     skyrim_mods.RuinsClutterImproved(),
    #     skyrim_mods.AlternateStart(),
    #     skyrim_mods.CinematicFireEffects(),
    #     skyrim_mods.HDEnhancedTerrain(),
    #     skyrim_mods.SkyrimDistanceOverhaul(),
    #     skyrim_mods.SkyrimDistanceOverhaulSkymillsPatch(),
    #     skyrim_mods.AnimatedDistantWaterfallsAndWindmills(),
    #     skyrim_mods.SkyrimHDFullVersion(),
    #     skyrim_mods.SkyrimCityBeautificationAllInOneByJK(),
    #     skyrim_mods.VividLandscapesDungeonsAndRuins(),
    #     skyrim_mods.VividLandscapesDungeonsAndRuinsSMIMPatch(),
    #     skyrim_mods.VividLandscapesVolcanicArea(),
    #     skyrim_mods.AMidianBornCavesAndMines2k(),
    #     skyrim_mods.ImmersiveRoads(),
    #     skyrim_mods.ImmersiveRoadsSnowShinePatch(),
    #     skyrim_mods.SkyrimFloraOverhaul(),
    #     skyrim_mods.SkyrimFloraOverhaulTallPines(),
    #     skyrim_mods.TreesHD(),
    #     skyrim_mods.SimplyBiggerTrees(),
    #     skyrim_mods.SimplyBiggerTreesSlowerBranches(),
    #     skyrim_mods.ParallaxTreebark4K(),
    #     skyrim_mods.ParallaxTreebark4KSimplyBiggerTreesPatch(),
    #     skyrim_mods.ImmersiveFallenTrees(),
    #     skyrim_mods.FencesOfSkyrim(),
    #     skyrim_mods.RusticWindows2K(),
    #     skyrim_mods.VerdantGrassPlugin(),
    #     skyrim_mods.VerdantGrassPluginDarkGrassTextureOption(),
    #     skyrim_mods.NaturalGrassTextureFloor(),
    #     skyrim_mods.RealVisionFloraPatch(),
    #     skyrim_mods.HighDefinitionIvy2K(),
    #     skyrim_mods.DetailedRugs(),
    #     skyrim_mods.PureWatersLegendaryEdition(),
    #     skyrim_mods.PureWatersLandscapeTextures(),
    #     skyrim_mods.VividLandscapesRockingStonesParallax(),
    #     skyrim_mods.VividLandscapesCliffsAndCreeks(),
    #     skyrim_mods.VividLandscapesRockingStonesCompatibilityPatch(),
    #     skyrim_mods.VividLandscapesTundraMossRevisited(),
    #     skyrim_mods.VividLandscapesTundraSMIMPatch(),
    #     skyrim_mods.VividLandscapesTundraMossMountainPatch(),
    #     skyrim_mods.FinerDust(),
    #     skyrim_mods.RealisticSmokeAndEmbers(),
    #     skyrim_mods.LanternsOfSkyrim()
    # ]

    # mods = [
    #     skyrim_mods.ParticlePatchForENB(),
    #     skyrim_mods.SubsurfaceScatteringPatchForENB()
    # ]

    # Install particle patches

    # pass 2
    # mods = [
    #     skyrim_mods.ParallaxTerrain4K(),
    #     skyrim_mods.CoastBeachTexturesForParallax(),
    #     skyrim_mods.PineForestTexturesForParallax(),
    #     skyrim_mods.ClimatesOfTamriel(),
    #     skyrim_mods.ClimatesOfTamrielSupremeStorms(),
    #     skyrim_mods.ClimatesOfTamrielWeatherPatch(),
    #     skyrim_mods.TrueStorms(),
    #     skyrim_mods.RealisticLightingOverhaul(),
    #     skyrim_mods.EnbSeriesV308(),
    #     skyrim_mods.RealVisionENB(),
    #     skyrim_mods.RealVisionFloraPatch(),
    #     skyrim_mods.ShowRaceMenuPrecacheKiller(),
    #     skyrim_mods.XeniusCharacterEnhancementFull(),
    #     skyrim_mods.ApachiiSkyHairFull(),
    #     skyrim_mods.ApachiiSkyHairFemale(),
    #     skyrim_mods.ApachiiSkyHairMale(),
    #     skyrim_mods.ApachiiSkyHairNaturalRetexture(),
    #     skyrim_mods.DimonizedUNPFemaleBody(),
    #     skyrim_mods.NoMoreBlockyFaces(),
    #     skyrim_mods.AllInOneFacePackUNP(),
    #     skyrim_mods.BetterMalesFace(),
    #     skyrim_mods.BetterMalesBody(),
    #     skyrim_mods.EyesOfBeauty(),
    #     skyrim_mods.HighDefinitionTeeth(),
    #     skyrim_mods.RealisticRagdollsAndForce(),
    #     # skyrim_mods.XVisionChildrenFixBubbleFace()
    # ]

    # Pass 3
    # mods = [
    #     skyrim_mods.InterestingNPCs(),
    #     skyrim_mods.WetAndColdRegularEdition(),
    #     skyrim_mods.WetAndColdAshes(),
    #     skyrim_mods.CompleteCampingSystem(),
    #     skyrim_mods.Tentapalooza(),
    #     skyrim_mods.FrostfallSurvival(),
    #     skyrim_mods.RealisticNeedsAndDiseases(),
    #     skyrim_mods.ImmersivePatrols(),
    #     skyrim_mods.TouringCarriages()
    # ]

    # mods = [
    #     skyrim_mods.TouringCarriages(),
    #     skyrim_mods.LanternsOfSkyrim()
    # ]
