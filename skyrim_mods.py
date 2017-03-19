###############################################################################
#   @description: Module containing mods for skyrim.
#   @author: Hayden McParlane
###############################################################################
from applogger import ModManagementLogger

log = ModManagementLogger()

import appconfig
import modcore
from modcore import ModBase
import management_engine
import os
from singleton import Singleton
import subprocess

class SkyrimMod(ModBase):
    def install_directory(self):
        return appconfig.SKYRIM_DATA_DIR

###############################################################################
# Environment/Graphic mods
###############################################################################
@Singleton
class DummyModToApplyStandardConfigurationChanges(SkyrimMod):
    def configurations(self):
        # IMPORTANT: These configurations may not be advisable for all computers. Mine is
        # fairly high end.
        return {
                # Allocated memory
                appconfig.SKYRIM_INI_FILE: {"Papyrus": {r"iMaxAllocatedMemoryBytes:"
                                                        r"Papyrus": 4294967295}},
                appconfig.SKYRIM_INI_FILE: {"General": {"fMasterFilePreLoadMB": 128.0000}},
                appconfig.SKYRIM_INI_FILE: {"General": {"iPreloadSizeLimit": 268435456}},

                # These configurations increase draw distance. Comment if machine isn't high end
                # Grid loading close
                appconfig.SKYRIM_INI_FILE: {"General": {"uGridsToLoad": 7}},
                appconfig.SKYRIM_INI_FILE: {"General": {"uInterior Cell Buffer": 32}},
                appconfig.SKYRIM_INI_FILE: {"General": {"uExterior Cell Buffer": 64}},

                # Loading in far distance
                # appconfig.SKYRIM_PREFS_INI_FILE: {"TerrainManager": {"fBlockLevel1Distance": 100000.0000}},
                # appconfig.SKYRIM_PREFS_INI_FILE: {"TerrainManager": {"fBlockLevel0Distance": 50000.0000}},
               }


@Singleton
class OptimizedVanillaTextures(SkyrimMod):
    def run_post_processing(self):
        install_script = "{0}/Textures Install.vbs".format(appconfig.SKYRIM_DATA_DIR)
        run_vb_script(install_script)

@Singleton
class UnofficialHighResolutionPatch(SkyrimMod):
    def dependencies(self):
        return (modcore.Dependency(self, OptimizedVanillaTextures.Instance()),)

@Singleton
class UnofficialSkyrimPatch(SkyrimMod):
    def dependencies(self):
        return (modcore.Dependency(self, UnofficialHighResolutionPatch.Instance()),)

@Singleton
class UnofficialHearthfirePatch(SkyrimMod):
    def dependencies(self):
        return (modcore.Dependency(self, UnofficialSkyrimPatch.Instance()),)

@Singleton
class UnofficialDragonbornPatch(SkyrimMod):
    def dependencies(self):
        return (modcore.Dependency(self, UnofficialSkyrimPatch.Instance()),)

@Singleton
class UnofficialDawnguardPatch(SkyrimMod):
    def dependencies(self):
        return (modcore.Dependency(self, UnofficialSkyrimPatch.Instance()),)

@Singleton
class UnofficialSkyrimLegendaryEditionPatch(SkyrimMod):
    def dependencies(self):
        return (modcore.Dependency(self, UnofficialHighResolutionPatch.Instance()),)

@Singleton
class StaticMeshImprovementMod(SkyrimMod):
    pass

@Singleton
class RuinsClutterImproved(SkyrimMod):
    pass

@Singleton
class AlternateStart(SkyrimMod):
    pass

@Singleton
class CinematicFireEffects(SkyrimMod):
    pass

@Singleton
class HDEnhancedTerrain(SkyrimMod):
    pass

@Singleton
class SkyrimDistanceOverhaul(SkyrimMod):
    # def configurations(self):
    #     return {appconfig.SKYRIM_PREFS_INI_FILE: {"TerrainManager": {"fBlockLevel1Distance": 70000 }},
    #             appconfig.SKYRIM_PREFS_INI_FILE: {"TerrainManager": {"fBlockLevel0Distance": 35000 }},}
    def configurations(self):
        return {appconfig.SKYRIM_PREFS_INI_FILE: {"TerrainManager": {"fBlockLevel1Distance": 120000 }},
                appconfig.SKYRIM_PREFS_INI_FILE: {"TerrainManager": {"fBlockLevel0Distance": 60000 }},}

@Singleton
class SkyrimDistanceOverhaulSkymillsPatch(SkyrimMod):
    def dependencies(self):
        return (modcore.Dependency(self, SkyrimDistanceOverhaul.Instance()),)

@Singleton
class AnimatedDistantWaterfallsAndWindmills(SkyrimMod):
    def patches(self):
        return (modcore.Patch(self, SkyrimDistanceOverhaulSkymillsPatch.Instance(), SkyrimDistanceOverhaul.Instance()),)

@Singleton
class SkyrimHDFullVersion(SkyrimMod):
    pass

@Singleton
class SkyrimCityBeautificationAllInOneByJK(SkyrimMod):
    def apply(self):
        # extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))
        # TODO: Come back to this mod. Seems like nexus is downloading incorrect archive size.
        pass


@Singleton
class VividLandscapesDungeonsAndRuins(SkyrimMod):

    def patches(self):
        return (modcore.Patch(self, VividLandscapesDungeonsAndRuinsSMIMPatch.Instance(),
                              StaticMeshImprovementMod.Instance()),)

    def configurations(self):
        return {appconfig.SKYRIM_INI_FILE: {"Display": {"bDeferredShadows": 1}},
                appconfig.SKYRIM_ENBLOCAL_INI_FILE: {"FIX": {"FixParallaxBugs": True}}}

@Singleton
class VividLandscapesDungeonsAndRuinsSMIMPatch(SkyrimMod):
    def dependencies(self):
        return (modcore.Dependency(self, VividLandscapesDungeonsAndRuins.Instance()),)

@Singleton
class VividLandscapesVolcanicArea(SkyrimMod):
    pass

@Singleton
class AMidianBornCavesAndMines2k(SkyrimMod):
    pass

@Singleton
class ImmersiveRoads(SkyrimMod):

    def configurations(self):
        return {appconfig.SKYRIM_ENBLOCAL_INI_FILE: {"FIX": {"FixParallaxBugs": True}},}

@Singleton
class ImmersiveRoadsReduceSnowShineTo40Percent(SkyrimMod):
    # TODO: May not need this. Snow too dark.
    def dependencies(self):
        return (modcore.Dependency(self, ImmersiveRoads.Instance()),)

@Singleton
class SkyrimFloraOverhaul(SkyrimMod):
    pass

@Singleton
class SkyrimFloraOverhaulTallPines(SkyrimMod):
    def dependencies(self):
        return (modcore.Dependency(self, SkyrimFloraOverhaul.Instance()),)

@Singleton
class TreesHD(SkyrimMod):
    pass

@Singleton
class SimplyBiggerTrees(SkyrimMod):
    pass

@Singleton
class SimplyBiggerTreesSlowerBranches(SkyrimMod):
    def dependencies(self):
        return (modcore.Dependency(self, SimplyBiggerTrees.Instance()),)

@Singleton
class ParallaxTreebark4K(SkyrimMod):
    def patches(self):
        return (modcore.Patch(self, ParallaxTreebark4KSimplyBiggerTreesPatch.Instance(), SimplyBiggerTrees.Instance()),)

@Singleton
class ParallaxTreebark4KSimplyBiggerTreesPatch(SkyrimMod):
    def dependencies(self):
        return (modcore.Dependency(self, ParallaxTreebark4K.Instance()),)

@Singleton
class ImmersiveFallenTrees(SkyrimMod):
    pass

@Singleton
class FencesOfSkyrim(SkyrimMod):
    pass

@Singleton
class RusticWindows2K(SkyrimMod):
    pass

@Singleton
class VerdantGrassPlugin(SkyrimMod):

    def configurations(self):
        return {appconfig.SKYRIM_INI_FILE: {"Grass": {"iMaxGrassTypesPerTexure": 15}},
                appconfig.SKYRIM_INI_FILE: {"Grass": {"iMinGrassSize": 60}},}

@Singleton
class VerdantGrassPluginDarkGrassTextureOption(SkyrimMod):
    def dependencies(self):
        return (modcore.Dependency(self, VerdantGrassPlugin.Instance()),)

@Singleton
class NaturalGrassTextureFloor(SkyrimMod):
    pass

@Singleton
class RealVisionFloraPatch(SkyrimMod):
    pass

@Singleton
class HighDefinitionIvy2K(SkyrimMod):
    pass

@Singleton
class DetailedRugs(SkyrimMod):
    pass

@Singleton
class PureWatersLegendaryEdition(SkyrimMod):
    pass

@Singleton
class PureWatersLandscapeTextures(SkyrimMod):
    pass

@Singleton
class VividLandscapesRockingStonesParallax(SkyrimMod):
    pass

@Singleton
class VividLandscapesRockingStonesParallaxGrey2K(SkyrimMod):
    pass

@Singleton
class VividLandscapesRockingStonesParallaxUncompressed2K(SkyrimMod):
    pass

@Singleton
class SuperiorRocksDarkGrey4K(SkyrimMod):
    pass

@Singleton
class SuperiorRocksLightGrey4K(SkyrimMod):
    pass

@Singleton
class SuperiorRocksLightGrey2K(SkyrimMod):
    pass

@Singleton
class RealMountainsRebuilt2KClassicLight(SkyrimMod):
    pass

@Singleton
class VividLandscapesCliffsAndCreeks(SkyrimMod):
    def patches(self):
        return (modcore.Patch(self, VividLandscapesRockingStonesCompatibilityPatch.Instance(),
                              VividLandscapesRockingStonesParallax.Instance()),)

@Singleton
class VividLandscapesRockingStonesCompatibilityPatch(SkyrimMod):
    def dependencies(self):
        return (modcore.Dependency(self, VividLandscapesRockingStonesParallax.Instance()),)

@Singleton
class VividLandscapesTundraMossRevisited(SkyrimMod):
    def patches(self):
        return (modcore.Patch(self, VividLandscapesTundraSMIMPatch.Instance(), StaticMeshImprovementMod.Instance()),
                modcore.Patch(self, VividLandscapesTundraMossMountainPatch.Instance(),
                              VividLandscapesRockingStonesParallax.Instance()))

@Singleton
class VividLandscapesTundraSMIMPatch(SkyrimMod):
    def dependencies(self):
        return (modcore.Dependency(self, VividLandscapesTundraMossRevisited.Instance()),
                modcore.Dependency(self, StaticMeshImprovementMod.Instance()),)

@Singleton
class VividLandscapesTundraMossMountainPatch(SkyrimMod):
    def dependencies(self):
        return (modcore.Dependency(self, VividLandscapesRockingStonesParallax.Instance()),)

@Singleton
class HorizonOfDreamsHDNightSky(SkyrimMod):
    pass

@Singleton
class FinerDust(SkyrimMod):
    pass

@Singleton
class RealisticSmokeAndEmbers(SkyrimMod):
    pass

@Singleton
class ParticlePatchForENB(SkyrimMod):
    def dependencies(self):
        return (modcore.Superiority(self, StaticMeshImprovementMod.Instance()),)

@Singleton
class SubsurfaceScatteringPatchForENB(SkyrimMod):
    def dependencies(self):
        return (modcore.Superiority(self, StaticMeshImprovementMod.Instance()),)

@Singleton
class ParallaxTerrain4K(SkyrimMod):
    pass

@Singleton
class CoastBeachTexturesForParallax(SkyrimMod):
    pass

@Singleton
class PineForestTexturesForParallax(SkyrimMod):
    pass

@Singleton
class ClimatesOfTamriel(SkyrimMod):
    pass

@Singleton
class ClimatesOfTamrielSupremeStorms(SkyrimMod):
    def dependencies(self):
        return (modcore.Dependency(self, ClimatesOfTamriel.Instance()),)

@Singleton
class ClimatesOfTamrielWeatherPatch(SkyrimMod):
    def dependencies(self):
        return (modcore.Dependency(self, ClimatesOfTamrielSupremeStorms.Instance()),)

@Singleton
class TrueStorms(SkyrimMod):
    pass

@Singleton
class RealisticLightingOverhaul(SkyrimMod):
    pass

@Singleton
class LanternsOfSkyrim(SkyrimMod):
    pass

@Singleton
class BlacksmithWaterFix(SkyrimMod):
    pass

# TODO: Separate Enb out from Skyrim-specific mod
@Singleton
class EnbSeriesV308(SkyrimMod):
    def install_directory(self):
        return appconfig.SKYRIM_BASE_DIR

@Singleton
class RealVisionENB(SkyrimMod):

    def run_post_processing(self):
        realvision_file_dir = "{0}/RealVision_ENB_files/{1}"
        install_script = realvision_file_dir.format(appconfig.SKYRIM_DATA_DIR, r"RV_install.vbe")
        set_ini_script = realvision_file_dir.format(appconfig.SKYRIM_DATA_DIR, r"RV_INIeditor.vbe")
        run_vb_script(install_script)
        run_vb_script(set_ini_script)

    def configurations(self):
        return {appconfig.SKYRIM_PREFS_INI_FILE: {"Display": {"bFloatPointRenderTarget": 1}},
                appconfig.SKYRIM_PREFS_INI_FILE: {"Display": {"bDrawLandShadows": 1}},
                appconfig.SKYRIM_PREFS_INI_FILE: {"Display": {"bTreesReceiveShadows": 1}},
                appconfig.SKYRIM_ENBLOCAL_INI_FILE: {"FIX": {"FixParallaxTerrain": True}},

                # Subsurface Skin Scattering
                appconfig.SKYRIM_ENBSERIES_INI_FILE: {"SUBSURFACESCATTERING": {"Quality": 0}},
                appconfig.SKYRIM_ENBSERIES_INI_FILE: {"SUBSURFACESCATTERING": {"Radius": 9.0}},
                appconfig.SKYRIM_ENBSERIES_INI_FILE: {"SUBSURFACESCATTERING": {"Amount": 0.35}},
                appconfig.SKYRIM_ENBSERIES_INI_FILE: {"SUBSURFACESCATTERING": {"EpidermalAmount": 7.0}},
                appconfig.SKYRIM_ENBSERIES_INI_FILE: {"SUBSURFACESCATTERING": {"SubdermalAmount": 7.0}},
                appconfig.SKYRIM_ENBSERIES_INI_FILE: {"SUBSURFACESCATTERING": {"EpidermalDiffuseSaturation": 0.88}},
                appconfig.SKYRIM_ENBSERIES_INI_FILE: {"SUBSURFACESCATTERING": {"SubdermalDiffuseSaturation": 0.88}},
                appconfig.SKYRIM_ENBSERIES_INI_FILE: {"SUBSURFACESCATTERING": {"EpidermalMix": 0.05}},
                appconfig.SKYRIM_ENBSERIES_INI_FILE: {"SUBSURFACESCATTERING": {"SubdermalMix": 1.0}},
                appconfig.SKYRIM_ENBSERIES_INI_FILE: {"SUBSURFACESCATTERING": {"SubdermalTranslucency": 0.1}},
                appconfig.SKYRIM_ENBSERIES_INI_FILE: {"SUBSURFACESCATTERING": {"SubdermalPhase": 0.69}},
                appconfig.SKYRIM_ENBSERIES_INI_FILE: {"EFFECT": {"EnableSubSurfaceScattering": True}},}

    def patches(self):
        return (modcore.Patch(self, RealVisionFloraPatch.Instance(), RealVisionENB.Instance()),)

    def dependencies(self):
        return (modcore.Dependency(self, EnbSeriesV308.Instance()),)

@Singleton
class TrueVisionENB(SkyrimMod):

    def run_post_processing(self):
        realvision_file_dir = "{0}/TrueVision_ENB_files/{1}"
        install_script = realvision_file_dir.format(appconfig.SKYRIM_DATA_DIR, r"RV_install.vbe")
        set_ini_script = realvision_file_dir.format(appconfig.SKYRIM_DATA_DIR, r"RV_INIeditor.vbe")
        run_vb_script(install_script)
        run_vb_script(set_ini_script)

    def configurations(self):
        return {appconfig.SKYRIM_PREFS_INI_FILE: {"Display": {"bFloatPointRenderTarget": 1}},
                appconfig.SKYRIM_PREFS_INI_FILE: {"Display": {"bDrawLandShadows": 1}},
                appconfig.SKYRIM_PREFS_INI_FILE: {"Display": {"bTreesReceiveShadows": 1}},
                appconfig.SKYRIM_ENBLOCAL_INI_FILE: {"FIX": {"FixParallaxTerrain": True}},

                # Subsurface Skin Scattering
                appconfig.SKYRIM_ENBSERIES_INI_FILE: {"SUBSURFACESCATTERING": {"Quality": 0}},
                appconfig.SKYRIM_ENBSERIES_INI_FILE: {"SUBSURFACESCATTERING": {"Radius": 9.0}},
                appconfig.SKYRIM_ENBSERIES_INI_FILE: {"SUBSURFACESCATTERING": {"Amount": 0.35}},
                appconfig.SKYRIM_ENBSERIES_INI_FILE: {"SUBSURFACESCATTERING": {"EpidermalAmount": 7.0}},
                appconfig.SKYRIM_ENBSERIES_INI_FILE: {"SUBSURFACESCATTERING": {"SubdermalAmount": 7.0}},
                appconfig.SKYRIM_ENBSERIES_INI_FILE: {"SUBSURFACESCATTERING": {"EpidermalDiffuseSaturation": 0.88}},
                appconfig.SKYRIM_ENBSERIES_INI_FILE: {"SUBSURFACESCATTERING": {"SubdermalDiffuseSaturation": 0.88}},
                appconfig.SKYRIM_ENBSERIES_INI_FILE: {"SUBSURFACESCATTERING": {"EpidermalMix": 0.05}},
                appconfig.SKYRIM_ENBSERIES_INI_FILE: {"SUBSURFACESCATTERING": {"SubdermalMix": 1.0}},
                appconfig.SKYRIM_ENBSERIES_INI_FILE: {"SUBSURFACESCATTERING": {"SubdermalTranslucency": 0.1}},
                appconfig.SKYRIM_ENBSERIES_INI_FILE: {"SUBSURFACESCATTERING": {"SubdermalPhase": 0.69}},
                appconfig.SKYRIM_ENBSERIES_INI_FILE: {"EFFECT": {"EnableSubSurfaceScattering": True}},}

    def dependencies(self):
        return (modcore.Dependency(self, EnbSeriesV308.Instance()),)

@Singleton
class RealVisionFloraPatch(SkyrimMod):
    def dependencies(self):
        return (modcore.Dependency(self, RealVisionENB.Instance()),)

@Singleton
class FootprintsInSnow(SkyrimMod):
    pass

@Singleton
class WondersOfWeatherRainDropSplashAndInteriorSounds(SkyrimMod):
    pass

@Singleton
class HighDefinitionCoins(SkyrimMod):
    pass

@Singleton
class IntricateSpiderWebs(SkyrimMod):
    pass

@Singleton
class HighDefinitionFoodAndIngredients(SkyrimMod):
    pass


###############################################################################
# Model mods
###############################################################################
@Singleton
class ShowRaceMenuPrecacheKiller(SkyrimMod):
    pass

@Singleton
class XeniusCharacterEnhancementFull(SkyrimMod):
    pass

@Singleton
class SuperiorLoreFriendlyHair(SkyrimMod):
    pass


@Singleton
class ApachiiSkyHairFull(SkyrimMod):
    pass

@Singleton
class ApachiiSkyHairFemale(SkyrimMod):
    def dependencies(self):
        return (modcore.Dependency(self, ApachiiSkyHairFull.Instance()),)

@Singleton
class ApachiiSkyHairMale(SkyrimMod):
    def dependencies(self):
        return (modcore.Dependency(self, ApachiiSkyHairFull.Instance()),)

@Singleton
class ApachiiSkyHairNaturalRetexture(SkyrimMod):
    def dependencies(self):
        return (modcore.Dependency(self, ApachiiSkyHairFull.Instance()),)

@Singleton
class DimonizedUNPFemaleBody(SkyrimMod):
    pass

@Singleton
class UNPMainFemaleBodyReplacer(SkyrimMod):
    pass

@Singleton
class AllInOneFacePackUNP(SkyrimMod):
    def dependencies(self):
        return (modcore.Dependency(self, DimonizedUNPFemaleBody.Instance()),)

@Singleton
class RealGirlsRealisticBodyTextureUNP(SkyrimMod):
    def dependencies(self):
        return (modcore.Dependency(self, DimonizedUNPFemaleBody.Instance()),)

@Singleton
class BetterMalesFace(SkyrimMod):
    pass

@Singleton
class BetterMalesBody(SkyrimMod):
    def dependencies(self):
        return (modcore.Dependency(self, BetterMalesFace.Instance()),)

@Singleton
class HighDefinitionTeeth(SkyrimMod):
    pass

@Singleton
class SkySightSkinsHDMaleTextures(SkyrimMod):
    pass

@Singleton
class EyesOfBeauty(SkyrimMod):
    pass

@Singleton
class EyesOfBeautyNPC(SkyrimMod):
    def dependencies(self):
        return (modcore.Dependency(self, EyesOfBeauty.Instance()),)

@Singleton
class RealisticRagdollsAndForce(SkyrimMod):
    pass

@Singleton
class SportySexySweat(SkyrimMod):
    pass

@Singleton
class MalesOfSkyrim(SkyrimMod):
    pass

@Singleton
class OrdinaryWomenOfSkyrim(SkyrimMod):
    pass

@Singleton
class HighDefinitionEyeBrows(SkyrimMod):
    pass

# class EnhancedCharacterEdit(SkyrimMod):
#     def apply(self):
#         extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

###############################################################################
# Immersion mods
###############################################################################
@Singleton
class SkyUI5(SkyrimMod):
    pass

@Singleton
class InterestingNPCs(SkyrimMod):
    pass

@Singleton
class WetAndColdRegularEdition(SkyrimMod):
    pass

@Singleton
class WetAndColdAshes(SkyrimMod):
    def dependencies(self):
        return (modcore.Dependency(self, WetAndColdRegularEdition.Instance()),)

@Singleton
class CompleteCampingSystem(SkyrimMod):
    pass

@Singleton
class Tentapalooza(SkyrimMod):
    def dependencies(self):
        return (modcore.Dependency(self, CompleteCampingSystem.Instance()),)

@Singleton
class FrostfallSurvival(SkyrimMod):
    def dependencies(self):
        return (modcore.Dependency(self, CompleteCampingSystem.Instance()),
                modcore.Dependency(self, BeltFastenedQuivers.Instance()),)

@Singleton
class RealisticNeedsAndDiseases(SkyrimMod):
    pass

@Singleton
class ImmersivePatrols(SkyrimMod):
    pass

@Singleton
class TouringCarriages(SkyrimMod):
    pass

@Singleton
class LanternsOfSkyrim(SkyrimMod):
    pass

@Singleton
class RSChildrenOverhaul(SkyrimMod):
    def patches(self):
        return (modcore.Patch(self, RSChildrenOverhaulUnofficialSkyrimPatch.Instance(), UnofficialSkyrimPatch.Instance()),
                modcore.Patch(self, RSChildrenOverhaulInterestingNPCPatch.Instance(), InterestingNPCs.Instance()),)

@Singleton
class RSChildrenOverhaulUnofficialSkyrimPatch(SkyrimMod):
    def dependencies(self):
        return (modcore.Dependency(self, RSChildrenOverhaul.Instance()),)

@Singleton
class RSChildrenOverhaulInterestingNPCPatch(SkyrimMod):
    def dependencies(self):
        return (modcore.Dependency(self, RSChildrenOverhaul.Instance()),
                modcore.Dependency(self, InterestingNPCs.Instance()),)

@Singleton
class ImmersiveHUD(SkyrimMod):
    pass

@Singleton
class ImmersiveWeapons(SkyrimMod):
    pass

@Singleton
class ImmersiveArmorsPart1(SkyrimMod):
    def dependencies(self):
        return (modcore.Dependency(self, ImmersiveArmorsPart2.Instance()),)

    def patches(self):
        return (modcore.Patch(self, ImmersiveArmorsUNPPatch.Instance(), DimonizedUNPFemaleBody.Instance()),)

@Singleton
class ImmersiveArmorsPart2(SkyrimMod):
    def patches(self):
        return (modcore.Patch(self, ImmersiveArmorsUNPPatch.Instance(), DimonizedUNPFemaleBody.Instance()),)

@Singleton
class ImmersiveArmorsUNPPatch(SkyrimMod):
    def dependencies(self):
        return (modcore.Dependency(self, ImmersiveArmorsPart1.Instance()),
                modcore.Dependency(self, ImmersiveArmorsPart2.Instance()),)

@Singleton
class QualityWorldMapPaperEdition(SkyrimMod):
    pass

@Singleton
class QualityWorldMapVividFlatRoadEdition(SkyrimMod):
    pass

@Singleton
class AmazingFollowerTweaks(SkyrimMod):
    pass

@Singleton
class DuelCombatRealism(SkyrimMod):
    pass


@Singleton
class HDArmoredCirclets(SkyrimMod):
    pass

@Singleton
class RiversideLodge(SkyrimMod):
    pass

@Singleton
class VividCloudsAndFogs(SkyrimMod):
    def patches(self):
        return (modcore.Patch(self, VividCloudsAndFogsClimatesOfTamrielPatch.Instance(), ClimatesOfTamriel.Instance()),)

@Singleton
class VividCloudsAndFogsClimatesOfTamrielPatch(SkyrimMod):
    def dependencies(self):
        return (modcore.Dependency(self, VividCloudsAndFogs.Instance()),)

@Singleton
class WearableLanterns(SkyrimMod):
    pass

@Singleton
class EnhancedBloodTextures(SkyrimMod):
    def patches(self):
        return (modcore.Patch(self, ImprovedCombatSoundsEnhancedBloodTexturesPatch.Instance(),
                              ImprovedCombatSounds.Instance()),)

@Singleton
class Warzones2015(SkyrimMod):
    pass

@Singleton
class ImprovedCombatSounds(SkyrimMod):
    pass

@Singleton
class ImprovedCombatSoundsEnhancedBloodTexturesPatch(SkyrimMod):
    def dependencies(self):
        return (modcore.Dependency(self, ImprovedCombatSounds.Instance()),)

@Singleton
class BeltFastenedQuivers(SkyrimMod):
    pass

@Singleton
class ImmersiveJewelry(SkyrimMod):
    pass

@Singleton
class RemoveLevelCapAt100(SkyrimMod):
    pass

@Singleton
class ReduceDistanceNPCGreeting(SkyrimMod):
    pass

@Singleton
class BuyableBusinessesAndRealEstate(SkyrimMod):
    pass


###############################################################################
#   Weapons/Armor mods
###############################################################################
@Singleton
class RealBows(SkyrimMod):
    pass

@Singleton
class PaladinArtifactsAndArmor(SkyrimMod):
    pass

@Singleton
class TemplarSet(SkyrimMod):
    pass

@Singleton
class WeaponsOfTheThirdEra(SkyrimMod):
    pass

@Singleton
class UniqueUniquesWeapons(SkyrimMod):
    pass

@Singleton
class JaysusSwords(SkyrimMod):
    pass

@Singleton
class GhosuWeaponPack(SkyrimMod):
    pass

@Singleton
class WarriorWithinWeapons(SkyrimMod):
    pass

@Singleton
class DreadKnightWeaponSet(SkyrimMod):
    pass

@Singleton
class LOTRWeapons(SkyrimMod):
    pass

@Singleton
class ApocalypseMagic(SkyrimMod):
    pass

@Singleton
class BookOfSilenceHDArmor(SkyrimMod):
    pass

@Singleton
class BookOfSilenceHDWeapons(SkyrimMod):
    pass

@Singleton
class WeaponRetextureProject(SkyrimMod):
    pass

@Singleton
class PerfectLegionnaireArmor(SkyrimMod):
    pass

@Singleton
class HighDefinitionArmoredCirclets4K(SkyrimMod):
    pass

@Singleton
class RealisticBowSounds(SkyrimMod):
    pass

###############################################################################
#   Animation mods
###############################################################################
@Singleton
class FNISAnimation(SkyrimMod):
    def run_post_processing(self):
        # TODO: add run of GenerateFNISforUsers?
        pass

@Singleton
class OSASkyrimAscendencyEngineForImmersiveAnimations(SkyrimMod):
    pass

@Singleton
class OSAnimations(SkyrimMod):
    def dependencies(self):
        return (modcore.Dependency(self, FNISAnimation.Instance()),
                modcore.Dependency(self, NetImmerseOverrideForSKSE.Instance()),
                modcore.Dependency(self, SkyUI5.Instance()),
                modcore.Dependency(self, OSASkyrimAscendencyEngineForImmersiveAnimations.Instance()),)


###############################################################################
#   Misc mods
###############################################################################
@Singleton
class NetImmerseOverrideForSKSE(SkyrimMod):
    def run_post_processing(self):
        pass

@Singleton
class PopulatedCities(SkyrimMod):
    def run_post_processing(self):
        pass

@Singleton
class HighDefinitionFood(SkyrimMod):
    pass

@Singleton
class HighDefinitionMiscellaneousItems(SkyrimMod):
    pass

@Singleton
class HighDefinitionWoodCuttersAxe(SkyrimMod):
    def patches(self):
        return (modcore.Patch(self, HighDefinitionWoodCuttersAxeFrostfallPatch.Instance(), FrostfallSurvival.Instance()),)

@Singleton
class HighDefinitionWoodCuttersAxeFrostfallPatch(SkyrimMod):
    def dependencies(self):
        return (modcore.Dependency(self, HighDefinitionWoodCuttersAxe.Instance()),)

@Singleton
class HighDefinitionBookCovers(SkyrimMod):
    pass

@Singleton
class FasterHorseSprint(SkyrimMod):
    pass

@Singleton
class HighDefinitionInsects(SkyrimMod):
    pass

@Singleton
class HighDefinitionDragons(SkyrimMod):
    pass

@Singleton
class HighDefinitionBeards(SkyrimMod):
    pass

@Singleton
class HighDefinitionGems(SkyrimMod):
    pass

@Singleton
class MainMenuReplacer(SkyrimMod):
    pass

@Singleton
class HighDefinitionMountains_RealMountains4KBrown(SkyrimMod):
    pass

@Singleton
class HighDefinitionMountains_RealMountains2KBrown(SkyrimMod):
    pass

@Singleton
class HighDefinitionMountains_RealMountains4KDefault(SkyrimMod):
    pass

@Singleton
class AddPlayerHome_AzuraDawnMansion(SkyrimMod):
    def patches(self):
        # Depends on hearthfire patch because this mod manager doesn't handle official DLCs.
        # But if the hearthfire patch is included, hearthfire must also be included.
        return (modcore.Patch(self, AddPlayerHome_AzuraDawnMansionHearthfirePatch.Instance(),
                              UnofficialHearthfirePatch.Instance()),)

@Singleton
class AddPlayerHome_AzuraDawnMansionHearthfirePatch(SkyrimMod):
    pass

@Singleton
class AddNewClothing_CommonClothes(SkyrimMod):
    pass

@Singleton
class AddCompanions_SkyCompanionsUNP(SkyrimMod):
    pass

@Singleton
class AddCompanions_Hoth(SkyrimMod):
    pass

@Singleton
class AddCompanions_DanarielStormbow(SkyrimMod):
    pass

@Singleton
class BalanceNPCSocialAtmosphere_InconsequentialNPC(SkyrimMod):
    pass

@Singleton
class ExtremelyDeadlyArrows_DeadlyArrows(SkyrimMod):
    pass

@Singleton
class AddBirdSpecies(SkyrimMod):
    pass

@Singleton
class RemoveFogFromMainMenuAndLoadScreens(SkyrimMod):
    pass

###############################################################################
#   Helper functions
###############################################################################
# todo: Is this needed after modcore changes?
def compressed_file(mod_name):
    return management_engine.compressed_file(appconfig.APP_MOD_DIR_SKYRIM, mod_name)

def run_vb_script(script_name):
    if os.path.exists(script_name):
        log.info("Running '{0}'".format(script_name))
        subprocess.call([r"cscript.exe", script_name])