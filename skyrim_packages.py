from modcore import ModPackage
import skyrim_mods

class SkyrimModPackage(ModPackage):
    pass

class FoundationPatchPack(SkyrimModPackage):
    def mods(self):
        return frozenset([
            skyrim_mods.UnofficialHighResolutionPatch(),
            skyrim_mods.UnofficialSkyrimPatch(),
            # skyrim_mods.UnofficialSkyrimLegendaryEditionPatch(),
            skyrim_mods.OptimizedVanillaTextures(),
            skyrim_mods.StaticMeshImprovementMod(),
            skyrim_mods.SkyUI5(),
        ])

class RealisticWorldWithRealVisionENB(SkyrimModPackage):

    # todo; remove environmental enhancements from high res pack. Enhancements should be separate.
    def mods(self):
        return frozenset([
            skyrim_mods.RuinsClutterImproved(),
            skyrim_mods.AlternateStart(),
            skyrim_mods.CinematicFireEffects(),
            skyrim_mods.HDEnhancedTerrain(),
            skyrim_mods.SkyrimDistanceOverhaul(),
            skyrim_mods.SkyrimDistanceOverhaulSkymillsPatch(),
            skyrim_mods.AnimatedDistantWaterfallsAndWindmills(),
            skyrim_mods.SkyrimHDFullVersion(),
            # skyrim_mods.SkyrimCityBeautificationAllInOneByJK(),
            skyrim_mods.VividLandscapesDungeonsAndRuins(),
            skyrim_mods.VividLandscapesDungeonsAndRuinsSMIMPatch(),
            skyrim_mods.VividLandscapesVolcanicArea(),
            skyrim_mods.AMidianBornCavesAndMines2k(),
            skyrim_mods.ImmersiveRoads(),
            skyrim_mods.ImmersiveRoadsReduceSnowShineTo40Percent(),
            skyrim_mods.SkyrimFloraOverhaul(),
            skyrim_mods.SkyrimFloraOverhaulTallPines(),
            skyrim_mods.TreesHD(),
            skyrim_mods.SimplyBiggerTrees(),
            skyrim_mods.SimplyBiggerTreesSlowerBranches(),
            skyrim_mods.ParallaxTreebark4K(),
            skyrim_mods.ParallaxTreebark4KSimplyBiggerTreesPatch(),
            skyrim_mods.ImmersiveFallenTrees(),
            skyrim_mods.FencesOfSkyrim(),
            skyrim_mods.RusticWindows2K(),
            skyrim_mods.VerdantGrassPlugin(),
            skyrim_mods.VerdantGrassPluginDarkGrassTextureOption(),
            skyrim_mods.NaturalGrassTextureFloor(),
            skyrim_mods.RealVisionFloraPatch(),
            skyrim_mods.HighDefinitionIvy2K(),
            skyrim_mods.DetailedRugs(),
            skyrim_mods.PureWatersLegendaryEdition(),
            skyrim_mods.PureWatersLandscapeTextures(),
            skyrim_mods.VividLandscapesRockingStonesParallax(),
            skyrim_mods.VividLandscapesCliffsAndCreeks(),
            skyrim_mods.VividLandscapesRockingStonesCompatibilityPatch(),
            skyrim_mods.VividLandscapesTundraMossRevisited(),
            skyrim_mods.VividLandscapesTundraSMIMPatch(),
            skyrim_mods.VividLandscapesTundraMossMountainPatch(),
            skyrim_mods.FinerDust(),
            skyrim_mods.RealisticSmokeAndEmbers(),
            skyrim_mods.LanternsOfSkyrim(),
            skyrim_mods.ParticlePatchForENB(), # todo: how to include ENB outside of this pack? It's not really related
            skyrim_mods.SubsurfaceScatteringPatchForENB(),
            skyrim_mods.ParallaxTerrain4K(),
            skyrim_mods.CoastBeachTexturesForParallax(),
            skyrim_mods.PineForestTexturesForParallax(),
            skyrim_mods.ClimatesOfTamriel(),
            skyrim_mods.ClimatesOfTamrielSupremeStorms(),
            skyrim_mods.ClimatesOfTamrielWeatherPatch(),
            skyrim_mods.TrueStorms(),
            skyrim_mods.RealisticLightingOverhaul(),
            skyrim_mods.EnbSeriesV308(),
            skyrim_mods.RealVisionENB(),
            skyrim_mods.RealVisionFloraPatch(),
            skyrim_mods.ShowRaceMenuPrecacheKiller(),
            skyrim_mods.XeniusCharacterEnhancementFull(),
            skyrim_mods.ApachiiSkyHairFull(),
            skyrim_mods.ApachiiSkyHairFemale(),
            skyrim_mods.ApachiiSkyHairMale(),
            skyrim_mods.ApachiiSkyHairNaturalRetexture(),
            skyrim_mods.DimonizedUNPFemaleBody(),
            skyrim_mods.AllInOneFacePackUNP(),
            skyrim_mods.BetterMalesFace(),
            skyrim_mods.BetterMalesBody(),
            skyrim_mods.EyesOfBeauty(),
            skyrim_mods.EyesOfBeautyNPC(),
            skyrim_mods.HighDefinitionTeeth(),
            skyrim_mods.RealisticRagdollsAndForce(),
        ])

class HarshSkyrimImmersionPack(SkyrimModPackage):
    def mods(self):
        return frozenset([
            skyrim_mods.InterestingNPCs(),
            skyrim_mods.WetAndColdRegularEdition(),
            skyrim_mods.WetAndColdAshes(),
            skyrim_mods.CompleteCampingSystem(),
            skyrim_mods.Tentapalooza(),
            skyrim_mods.FrostfallSurvival(),
            skyrim_mods.RealisticNeedsAndDiseases(),
            skyrim_mods.ImmersivePatrols(),
            skyrim_mods.TouringCarriages(),
        ])

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
