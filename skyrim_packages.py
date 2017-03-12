from modcore import ModPackage
import skyrim_mods

class SkyrimModPackage(ModPackage):
    pass

class FoundationPatchPack(SkyrimModPackage):
    def mods(self):
        return (
            skyrim_mods.UnofficialHighResolutionPatch.Instance(),
            skyrim_mods.UnofficialSkyrimPatch.Instance(),
            skyrim_mods.UnofficialDawnguardPatch.Instance(),
            skyrim_mods.UnofficialHearthfirePatch.Instance(),
            skyrim_mods.UnofficialDragonbornPatch.Instance(),
            # skyrim_mods.UnofficialSkyrimLegendaryEditionPatch.Instance(),
            skyrim_mods.OptimizedVanillaTextures.Instance(),
            skyrim_mods.StaticMeshImprovementMod.Instance(),
            skyrim_mods.SkyUI5.Instance(),
        )

class RealisticWorldWithRealVisionENB(SkyrimModPackage):

    # todo; remove environmental enhancements from high res pack. Enhancements should be separate.
    # TODO: Eliminate patch definitions. Patches should be auto-handled by installer. Need to ensure
    # TODO: correctness of that subsystem.
    def mods(self):
        return (
            # Environment models/textures
            skyrim_mods.RuinsClutterImproved.Instance(),
            skyrim_mods.CinematicFireEffects.Instance(),
            skyrim_mods.HDEnhancedTerrain.Instance(),
            skyrim_mods.SkyrimDistanceOverhaul.Instance(),
            skyrim_mods.AnimatedDistantWaterfallsAndWindmills.Instance(),
            skyrim_mods.SkyrimHDFullVersion.Instance(),
            # skyrim_mods.SkyrimCityBeautificationAllInOneByJK.Instance(),
            skyrim_mods.VividLandscapesDungeonsAndRuins.Instance(),
            skyrim_mods.VividLandscapesVolcanicArea.Instance(),
            skyrim_mods.QualityWorldMapVividFlatRoadEdition.Instance(),
            skyrim_mods.AMidianBornCavesAndMines2k.Instance(),
            skyrim_mods.ImmersiveRoads.Instance(),
            skyrim_mods.ImmersiveRoadsReduceSnowShineTo40Percent.Instance(),
            skyrim_mods.SkyrimFloraOverhaul.Instance(),
            skyrim_mods.SkyrimFloraOverhaulTallPines.Instance(),
            skyrim_mods.TreesHD.Instance(),
            skyrim_mods.SimplyBiggerTrees.Instance(),
            skyrim_mods.SimplyBiggerTreesSlowerBranches.Instance(),
            skyrim_mods.ParallaxTreebark4K.Instance(),
            skyrim_mods.ImmersiveFallenTrees.Instance(),
            skyrim_mods.FencesOfSkyrim.Instance(),
            skyrim_mods.RusticWindows2K.Instance(),
            skyrim_mods.VerdantGrassPlugin.Instance(),
            skyrim_mods.VerdantGrassPluginDarkGrassTextureOption.Instance(),
            skyrim_mods.NaturalGrassTextureFloor.Instance(),
            skyrim_mods.HighDefinitionIvy2K.Instance(),
            skyrim_mods.DetailedRugs.Instance(),
            skyrim_mods.PureWatersLegendaryEdition.Instance(),
            skyrim_mods.PureWatersLandscapeTextures.Instance(),
            skyrim_mods.WondersOfWeatherRainDropSplashAndInteriorSounds.Instance(),
            # skyrim_mods.VividLandscapesRockingStonesParallax.Instance(), TODO: Pick this one or one below
            skyrim_mods.SuperiorRocksLightGrey4K.Instance(),
            skyrim_mods.VividLandscapesCliffsAndCreeks.Instance(),
            skyrim_mods.VividLandscapesTundraMossRevisited.Instance(),
            # skyrim_mods.VividCloudsAndFogs.Instance(),
            skyrim_mods.HorizonOfDreamsHDNightSky.Instance(),
            skyrim_mods.FinerDust.Instance(),
            skyrim_mods.RealisticSmokeAndEmbers.Instance(),
            skyrim_mods.LanternsOfSkyrim.Instance(),
            skyrim_mods.BlacksmithWaterFix.Instance(),
            skyrim_mods.HDArmoredCirclets.Instance(),
            skyrim_mods.IntricateSpiderWebs.Instance(),
            skyrim_mods.RiversideLodge.Instance(),
            skyrim_mods.ParticlePatchForENB.Instance(), # todo: how to include ENB outside of this pack? It's not really related
            skyrim_mods.SubsurfaceScatteringPatchForENB.Instance(),
            skyrim_mods.ParallaxTerrain4K.Instance(),
            skyrim_mods.HighDefinitionCoins.Instance(),
            skyrim_mods.CoastBeachTexturesForParallax.Instance(),
            skyrim_mods.PineForestTexturesForParallax.Instance(),
            skyrim_mods.ClimatesOfTamriel.Instance(),
            skyrim_mods.ClimatesOfTamrielSupremeStorms.Instance(),
            skyrim_mods.ClimatesOfTamrielWeatherPatch.Instance(),
            skyrim_mods.TrueStorms.Instance(),
            skyrim_mods.EnhancedBloodTextures.Instance(),
            skyrim_mods.FootprintsInSnow.Instance(),
            skyrim_mods.RealisticLightingOverhaul.Instance(),
            skyrim_mods.EnbSeriesV308.Instance(),
            skyrim_mods.RealVisionENB.Instance(),
            skyrim_mods.RealVisionFloraPatch.Instance(),
            skyrim_mods.HighDefinitionFoodAndIngredients.Instance(),
        )

class RealisticWorldWithTrueVisionENB(SkyrimModPackage):

    # todo; remove environmental enhancements from high res pack. Enhancements should be separate.
    # TODO: Eliminate patch definitions. Patches should be auto-handled by installer. Need to ensure
    # TODO: correctness of that subsystem.
    def mods(self):
        return (
            # Environment models/textures
            skyrim_mods.RuinsClutterImproved.Instance(),
            skyrim_mods.CinematicFireEffects.Instance(),
            skyrim_mods.HDEnhancedTerrain.Instance(),
            skyrim_mods.SkyrimDistanceOverhaul.Instance(),
            skyrim_mods.AnimatedDistantWaterfallsAndWindmills.Instance(),
            skyrim_mods.SkyrimHDFullVersion.Instance(),
            # skyrim_mods.SkyrimCityBeautificationAllInOneByJK.Instance(),
            skyrim_mods.VividLandscapesDungeonsAndRuins.Instance(),
            skyrim_mods.VividLandscapesVolcanicArea.Instance(),
            skyrim_mods.QualityWorldMapVividFlatRoadEdition.Instance(),
            skyrim_mods.AMidianBornCavesAndMines2k.Instance(),
            skyrim_mods.ImmersiveRoads.Instance(),
            skyrim_mods.ImmersiveRoadsReduceSnowShineTo40Percent.Instance(),
            skyrim_mods.SkyrimFloraOverhaul.Instance(),
            skyrim_mods.SkyrimFloraOverhaulTallPines.Instance(),
            skyrim_mods.TreesHD.Instance(),
            skyrim_mods.SimplyBiggerTrees.Instance(),
            skyrim_mods.SimplyBiggerTreesSlowerBranches.Instance(),
            skyrim_mods.ParallaxTreebark4K.Instance(),
            skyrim_mods.ImmersiveFallenTrees.Instance(),
            skyrim_mods.FencesOfSkyrim.Instance(),
            skyrim_mods.RusticWindows2K.Instance(),
            skyrim_mods.VerdantGrassPlugin.Instance(),
            skyrim_mods.VerdantGrassPluginDarkGrassTextureOption.Instance(),
            skyrim_mods.NaturalGrassTextureFloor.Instance(),
            skyrim_mods.HighDefinitionIvy2K.Instance(),
            skyrim_mods.DetailedRugs.Instance(),
            skyrim_mods.PureWatersLegendaryEdition.Instance(),
            skyrim_mods.PureWatersLandscapeTextures.Instance(),
            skyrim_mods.WondersOfWeatherRainDropSplashAndInteriorSounds.Instance(),
            # skyrim_mods.VividLandscapesRockingStonesParallax.Instance(), TODO: Pick this one or one below
            skyrim_mods.SuperiorRocksDarkGrey4K.Instance(),
            skyrim_mods.VividLandscapesCliffsAndCreeks.Instance(),
            skyrim_mods.VividLandscapesTundraMossRevisited.Instance(),
            # skyrim_mods.VividCloudsAndFogs.Instance(),
            skyrim_mods.HorizonOfDreamsHDNightSky.Instance(),
            skyrim_mods.FinerDust.Instance(),
            skyrim_mods.RealisticSmokeAndEmbers.Instance(),
            skyrim_mods.LanternsOfSkyrim.Instance(),
            skyrim_mods.BlacksmithWaterFix.Instance(),
            skyrim_mods.HighDefinitionArmoredCirclets4K.Instance(),
            skyrim_mods.IntricateSpiderWebs.Instance(),
            skyrim_mods.RiversideLodge.Instance(),
            skyrim_mods.ParticlePatchForENB.Instance(), # todo: how to include ENB outside of this pack? It's not really related
            skyrim_mods.SubsurfaceScatteringPatchForENB.Instance(),
            skyrim_mods.ParallaxTerrain4K.Instance(),
            skyrim_mods.HighDefinitionCoins.Instance(),
            skyrim_mods.CoastBeachTexturesForParallax.Instance(),
            skyrim_mods.PineForestTexturesForParallax.Instance(),
            skyrim_mods.ClimatesOfTamriel.Instance(),
            skyrim_mods.ClimatesOfTamrielSupremeStorms.Instance(),
            skyrim_mods.ClimatesOfTamrielWeatherPatch.Instance(),
            skyrim_mods.TrueStorms.Instance(),
            skyrim_mods.EnhancedBloodTextures.Instance(),
            skyrim_mods.FootprintsInSnow.Instance(),
            skyrim_mods.RealisticLightingOverhaul.Instance(),
            skyrim_mods.EnbSeriesV308.Instance(),
            skyrim_mods.TrueVisionENB.Instance(),
            skyrim_mods.HighDefinitionFoodAndIngredients.Instance(),
            skyrim_mods.PopulatedCities.Instance(),
            skyrim_mods.HighDefinitionFood.Instance(),
            skyrim_mods.HighDefinitionMiscellaneousItems.Instance(),
            skyrim_mods.HighDefinitionWoodCuttersAxe.Instance(),
            skyrim_mods.HighDefinitionBookCovers.Instance(),
            skyrim_mods.HighDefinitionInsects.Instance(),
            skyrim_mods.HighDefinitionDragons.Instance(),
            skyrim_mods.AddBirdSpecies.Instance(),
        )

class ActorModelAndTexturePack(SkyrimModPackage):
    def mods(self):
        return (skyrim_mods.ShowRaceMenuPrecacheKiller.Instance(),
                skyrim_mods.XeniusCharacterEnhancementFull.Instance(),
                skyrim_mods.SuperiorLoreFriendlyHair.Instance(),
                skyrim_mods.ApachiiSkyHairFull.Instance(),
                skyrim_mods.ApachiiSkyHairFemale.Instance(),
                skyrim_mods.ApachiiSkyHairMale.Instance(),
                skyrim_mods.ApachiiSkyHairNaturalRetexture.Instance(),
                skyrim_mods.DimonizedUNPFemaleBody.Instance(),
                skyrim_mods.AllInOneFacePackUNP.Instance(),
                skyrim_mods.SportySexySweat.Instance(),
                # skyrim_mods.BetterMalesFace.Instance(),
                # skyrim_mods.BetterMalesBody.Instance(),
                skyrim_mods.SkySightSkinsHDMaleTextures.Instance(),
                skyrim_mods.EyesOfBeauty.Instance(),
                skyrim_mods.EyesOfBeautyNPC.Instance(),
                skyrim_mods.HighDefinitionEyeBrows.Instance(),
                skyrim_mods.HighDefinitionTeeth.Instance(),
                skyrim_mods.RealisticRagdollsAndForce.Instance(),
                skyrim_mods.OrdinaryWomenOfSkyrim.Instance(),
                skyrim_mods.MalesOfSkyrim.Instance(),
                skyrim_mods.HighDefinitionBeards.Instance(),)

class HarshSkyrimImmersionPack(SkyrimModPackage):
    def mods(self):
        return (
            skyrim_mods.AlternateStart.Instance(),
            skyrim_mods.InterestingNPCs.Instance(),
            skyrim_mods.WetAndColdRegularEdition.Instance(),
            skyrim_mods.WetAndColdAshes.Instance(),
            skyrim_mods.CompleteCampingSystem.Instance(),
            skyrim_mods.Tentapalooza.Instance(),
            skyrim_mods.FrostfallSurvival.Instance(),
            skyrim_mods.RealisticNeedsAndDiseases.Instance(),
            skyrim_mods.ImmersivePatrols.Instance(),
            skyrim_mods.TouringCarriages.Instance(),
            skyrim_mods.RSChildrenOverhaul.Instance(),
            skyrim_mods.ImmersiveHUD.Instance(),
            skyrim_mods.ImmersiveArmorsPart1.Instance(),
            skyrim_mods.ImmersiveArmorsPart2.Instance(),
            skyrim_mods.ImmersiveWeapons.Instance(),
            skyrim_mods.WearableLanterns.Instance(),
            skyrim_mods.AmazingFollowerTweaks.Instance(),
            skyrim_mods.DuelCombatRealism.Instance(),
            skyrim_mods.Warzones2015.Instance(),
            skyrim_mods.ImprovedCombatSounds.Instance(),
            skyrim_mods.ImmersiveJewelry.Instance(),
            skyrim_mods.RemoveLevelCapAt100.Instance(),
            skyrim_mods.ReduceDistanceNPCGreeting.Instance(),
            skyrim_mods.BuyableBusinessesAndRealEstate.Instance(),
            skyrim_mods.FasterHorseSprint.Instance(),
        )

class WeaponAndArmorPack(SkyrimModPackage):
    def mods(self):
        return (skyrim_mods.BookOfSilenceHDArmor.Instance(),
                skyrim_mods.WeaponRetextureProject.Instance(),
                skyrim_mods.PaladinArtifactsAndArmor.Instance(),
                skyrim_mods.RealBows.Instance(),
                skyrim_mods.TemplarSet.Instance(),
                skyrim_mods.WeaponsOfTheThirdEra.Instance(),
                skyrim_mods.BlacksmithWaterFix.Instance(),
                skyrim_mods.JaysusSwords.Instance(),
                skyrim_mods.UniqueUniquesWeapons.Instance(),
                skyrim_mods.GhosuWeaponPack.Instance(),
                skyrim_mods.WarriorWithinWeapons.Instance(),
                skyrim_mods.DreadKnightWeaponSet.Instance(),
                skyrim_mods.LOTRWeapons.Instance(),
                skyrim_mods.ApocalypseMagic.Instance(),
                skyrim_mods.PerfectLegionnaireArmor.Instance(),
                skyrim_mods.RealisticBowSounds.Instance(),)

class AnimationFoundationPack(SkyrimModPackage):
    def mods(self):
        return (skyrim_mods.FNISAnimation.Instance(),)

class ImmersiveAnimationPack(SkyrimModPackage):
    def mods(self):
        return (skyrim_mods.OSAnimations.Instance(),)

class TestPackage(SkyrimModPackage):
    def mods(self):
        return (
            skyrim_mods.HighDefinitionBeards.Instance(),
        )

