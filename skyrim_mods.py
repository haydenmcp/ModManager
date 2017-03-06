###############################################################################
#   @description: Module containing mods for skyrim.
#   @author: Hayden McParlane
###############################################################################
from applogger import ModiLogger

log = ModiLogger()

import appconfig
import modcore
from modcore import ModBase
import management_engine
import os
from singleton import Singleton
import subprocess
from zipfile import ZipFile


class SkyrimMod(ModBase):
    def install_directory(self):
        return appconfig.SKYRIM_DATA_DIRECTORY


###############################################################################
# Environment/Graphic mods
###############################################################################
@Singleton
class OptimizedVanillaTextures(SkyrimMod):
    def run_post_processing(self):
        log.info("Running 'Textures Install.vbs'")
        install_script = "{0}/Textures Install.vbs".format(appconfig.SKYRIM_DATA_DIRECTORY)
        if os.path.exists(install_script):
            subprocess.call(["cscript.exe", install_script])

@Singleton
class UnofficialHighResolutionPatch(SkyrimMod):
    def dependencies(self):
        return (modcore.Dependency(self, OptimizedVanillaTextures.Instance()),)

@Singleton
class UnofficialSkyrimPatch(SkyrimMod):
    def dependencies(self):
        return (modcore.Dependency(self, UnofficialHighResolutionPatch.Instance()),)

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
    pass

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

    # TODO: Move to configuration function?
    def run_post_processing(self):
        upsert_configuration(r"SkyrimPrefs.ini", {"bDeferredShadows": 1})
        upsert_configuration(r"enblocal.ini", {"FixParallaxBugs": True})

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

    def run_post_processing(self):
        upsert_configuration(r"enblocal.ini", {"FixParallaxBugs": True})

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
    def run_post_processing(self):
        upsert_configuration(r"Skyrim.ini", {"iMaxGrassTypesPerTexure": 15})  # TODO: Add [Grass] section
        upsert_configuration(r"Skyrim.ini", {"iMinGrassSize": 60})

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
        return appconfig.STEAM_SKYRIM_DIRECTORY

@Singleton
class RealVisionENB(SkyrimMod):

    # TODO: Use realvision auto-installer after extraction. currently, file modifications don't take place.
    def run_post_processing(self):
        log.info("Running 'RV_launcher.exe'")
        install_script = "{0}/RealVision_ENB_files/RV_launcher.exe".format(appconfig.SKYRIM_DATA_DIRECTORY)
        if os.path.exists(install_script):
            subprocess.call([install_script])

    def patches(self):
        return (modcore.Patch(self, RealVisionFloraPatch.Instance(), RealVisionENB.Instance()),)

    def dependencies(self):
        return (modcore.Dependency(self, EnbSeriesV308.Instance()),)


@Singleton
class RealVisionFloraPatch(SkyrimMod):
    def dependencies(self):
        return (modcore.Dependency(self, RealVisionENB.Instance()),)

@Singleton
class FootprintsInSnow(SkyrimMod):
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

# @Singleton
# class SkySightSkinsHDMaleTextures(SkyrimMod):
#     pass

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
        return (modcore.Dependency(self, CompleteCampingSystem.Instance()),)

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
        return (modcore.Patch(self, RSChildrenOverhaulUnofficialSkyrimPatch.Instance(), UnofficialSkyrimPatch.Instance()),)

@Singleton
class RSChildrenOverhaulUnofficialSkyrimPatch(SkyrimMod):
    def dependencies(self):
        return (modcore.Dependency(self, RSChildrenOverhaul.Instance()),)

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
class AmazingFollowerTweaks(SkyrimMod):
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

###############################################################################
#   Helper functions
###############################################################################
# todo: Is this needed after modcore changes?
def compressed_file(mod_name):
    return management_engine.compressed_file(appconfig.SKYRIM_APP_MOD_DIRECTORY, mod_name)


def extract_to_skyrim_data_folder(zip_file_name):
    log.info("Extracting Mod Contents to {0}".format(appconfig.SKYRIM_DATA_DIRECTORY))
    with ZipFile(zip_file_name) as archive:
        archive.extractall(appconfig.SKYRIM_DATA_DIRECTORY)


def extract_to_skyrim_base_folder(zip_file_name):
    log.info("Extracting Mod Contents to {0}".format(appconfig.STEAM_SKYRIM_DIRECTORY))
    with ZipFile(zip_file_name) as archive:
        archive.extractall(appconfig.STEAM_SKYRIM_DIRECTORY)


_file_to_configuration_mappings = dict()


def upsert_configuration(filename, configurations):
    # This function should wait until all mods are installed and should track
    # all needed changes to the files before actually reading in the file and
    # making the changes. This'll really optimize the update process.
    pass
