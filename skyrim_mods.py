###############################################################################
#   @description: Module containing mods for skyrim.
#   @author: Hayden McParlane
###############################################################################
from applogger import ModiLogger

log = ModiLogger()

import appconfig
import modbase
from modbase import ModBase
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
        return (modbase.Dependency(self, OptimizedVanillaTextures()),)


@Singleton
class UnofficialSkyrimPatch(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, UnofficialHighResolutionPatch()),)


@Singleton
class UnofficialSkyrimLegendaryEditionPatch(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, UnofficialHighResolutionPatch()),)


@Singleton
class StaticMeshImprovementMod(SkyrimMod):
    # TODO: This can have a dependency on either Unofficial Skyrim Patch or
    # TODO: UnofficialSkyrimLegendaryEditionPatch. How to resolve?
    def dependencies(self):
        return (modbase.Dependency(self, UnofficialSkyrimPatch()),)


@Singleton
class RuinsClutterImproved(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, StaticMeshImprovementMod()),)


@Singleton
class AlternateStart(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, RuinsClutterImproved()),)


@Singleton
class CinematicFireEffects(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, AlternateStart()),)


@Singleton
class HDEnhancedTerrain(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, CinematicFireEffects()),)


@Singleton
class SkyrimDistanceOverhaul(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, HDEnhancedTerrain()),)


@Singleton
class SkyrimDistanceOverhaulSkymillsPatch(SkyrimMod):
    # TODO: Patches should be a part of main mod. How to resolve?
    def dependencies(self):
        return (modbase.Dependency(self, SkyrimDistanceOverhaul()),)


@Singleton
class AnimatedDistantWaterfallsAndWindmills(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, SkyrimDistanceOverhaulSkymillsPatch()),)


@Singleton
class SkyrimHDFullVersion(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, AnimatedDistantWaterfallsAndWindmills()),)


@Singleton
class SkyrimCityBeautificationAllInOneByJK(SkyrimMod):
    def apply(self):
        # extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))
        # TODO: Come back to this mod. Seems like nexus is downloading incorrect archive size.
        pass


@Singleton
class VividLandscapesDungeonsAndRuins(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, SkyrimHDFullVersion()),)

    # TODO: Move to configuration function?
    def run_post_processing(self):
        upsert_configuration(r"SkyrimPrefs.ini", {"bDeferredShadows": 1})
        upsert_configuration(r"enblocal.ini", {"FixParallaxBugs": True})


@Singleton
class VividLandscapesDungeonsAndRuinsSMIMPatch(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, VividLandscapesDungeonsAndRuins()),)


@Singleton
class VividLandscapesVolcanicArea(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, VividLandscapesDungeonsAndRuinsSMIMPatch()),)


@Singleton
class AMidianBornCavesAndMines2k(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, VividLandscapesVolcanicArea()),)


@Singleton
class ImmersiveRoads(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, AMidianBornCavesAndMines2k()),)

    def run_post_processing(self):
        upsert_configuration(r"enblocal.ini", {"FixParallaxBugs": True})


@Singleton
class ImmersiveRoadsSnowShinePatch(SkyrimMod):
    # TODO: May not need this. Snow too dark.
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))


@Singleton
class SkyrimFloraOverhaul(SkyrimMod):
    # TODO: Patch above isn't used. If desired, this dependency needs to be updated.
    def dependencies(self):
        return (modbase.Dependency(self, ImmersiveRoads()),)


@Singleton
class SkyrimFloraOverhaulTallPines(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, SkyrimFloraOverhaul()),)


@Singleton
class TreesHD(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, SkyrimFloraOverhaulTallPines()),)


@Singleton
class SimplyBiggerTrees(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, TreesHD()),)


@Singleton
class SimplyBiggerTreesSlowerBranches(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, SimplyBiggerTrees()),)


@Singleton
class ParallaxTreebark4K(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, SimplyBiggerTreesSlowerBranches()),)


@Singleton
class ParallaxTreebark4KSimplyBiggerTreesPatch(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, ParallaxTreebark4K()),)


@Singleton
class ImmersiveFallenTrees(SkyrimMod):
    # TODO: This dependency is purely for flow of install. Clearly this isn't a
    # TODO: dependency of this mod. Need to redesign.
    def dependencies(self):
        return (modbase.Dependency(self, ParallaxTreebark4KSimplyBiggerTreesPatch()),)


@Singleton
class FencesOfSkyrim(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, ImmersiveFallenTrees()),)


@Singleton
class RusticWindows2K(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, FencesOfSkyrim()),)


@Singleton
class VerdantGrassPlugin(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, RusticWindows2K()),)

    def run_post_processing(self):
        upsert_configuration(r"Skyrim.ini", {"iMaxGrassTypesPerTexure": 15})  # TODO: Add [Grass] section
        upsert_configuration(r"Skyrim.ini", {"iMinGrassSize": 60})


@Singleton
class VerdantGrassPluginDarkGrassTextureOption(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, VerdantGrassPlugin()),)


@Singleton
class NaturalGrassTextureFloor(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, VerdantGrassPluginDarkGrassTextureOption()),)


@Singleton
class RealVisionFloraPatch(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, NaturalGrassTextureFloor()),)


@Singleton
class HighDefinitionIvy2K(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, RealVisionFloraPatch()),)


@Singleton
class DetailedRugs(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, HighDefinitionIvy2K()),)


@Singleton
class PureWatersLegendaryEdition(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, DetailedRugs()),)


@Singleton
class PureWatersLandscapeTextures(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, PureWatersLegendaryEdition()),)


@Singleton
class VividLandscapesRockingStonesParallax(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, PureWatersLandscapeTextures()),)


@Singleton
class VividLandscapesCliffsAndCreeks(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, VividLandscapesRockingStonesParallax()),)


@Singleton
class VividLandscapesRockingStonesCompatibilityPatch(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, VividLandscapesCliffsAndCreeks()),)


@Singleton
class VividLandscapesTundraMossRevisited(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, VividLandscapesRockingStonesCompatibilityPatch()),)


@Singleton
class VividLandscapesTundraSMIMPatch(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, VividLandscapesTundraMossRevisited()),)


@Singleton
class VividLandscapesTundraMossMountainPatch(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, VividLandscapesTundraSMIMPatch()),)


@Singleton
class FinerDust(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, VividLandscapesTundraMossMountainPatch()),)


@Singleton
class RealisticSmokeAndEmbers(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, FinerDust()),)


@Singleton
class ParticlePatchForENB(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, RealisticSmokeAndEmbers()),
                modbase.Superiority(self, StaticMeshImprovementMod()))


@Singleton
class SubsurfaceScatteringPatchForENB(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, ParticlePatchForENB()),
                modbase.Superiority(self, StaticMeshImprovementMod()))


@Singleton
class ParallaxTerrain4K(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, SubsurfaceScatteringPatchForENB()),)


@Singleton
class CoastBeachTexturesForParallax(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, ParallaxTerrain4K()),)


@Singleton
class PineForestTexturesForParallax(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, CoastBeachTexturesForParallax()),)


@Singleton
class ClimatesOfTamriel(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, PineForestTexturesForParallax()),)


@Singleton
class ClimatesOfTamrielSupremeStorms(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, ClimatesOfTamriel()),)


@Singleton
class ClimatesOfTamrielWeatherPatch(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, ClimatesOfTamrielSupremeStorms()),)


@Singleton
class TrueStorms(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, ClimatesOfTamrielWeatherPatch()),)


@Singleton
class RealisticLightingOverhaul(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, TrueStorms()),)


@Singleton
class LanternsOfSkyrim(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, RealisticLightingOverhaul()),)


# TODO: Separate Enb out from Skyrim-specific mod
@Singleton
class EnbSeriesV308(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, LanternsOfSkyrim()),)


@Singleton
class RealVisionENB(SkyrimMod):
    # def apply(self):
    #     # TODO: After this extraction runs, need to run installer for realvision.
    #     # TODO: Make specified file modification under RealVision ENB manual install.
    #     extract_to_skyrim_b
    # ase_folder(compressed_file(self.__class__.__name__))

    # TODO: Use realvision auto-installer after extraction. currently, file modifications don't take place.
    def run_post_processing(self):
        log.info("Running 'Textures Install.vbs'")
        install_script = "{0}/Textures Install.vbs".format(appconfig.SKYRIM_DATA_DIRECTORY)
        if os.path.exists(install_script):
            subprocess.call(["cscript.exe", install_script])

    def dependencies(self):
        return (modbase.Dependency(self, EnbSeriesV308()),)


@Singleton
class RealVisionFloraPatch(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, RealVisionENB()),)


###############################################################################
# Model mods
###############################################################################
@Singleton
class ShowRaceMenuPrecacheKiller(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, RealVisionFloraPatch()),)


@Singleton
class XeniusCharacterEnhancementFull(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, ShowRaceMenuPrecacheKiller()),)


@Singleton
class ApachiiSkyHairFull(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, XeniusCharacterEnhancementFull()),)


@Singleton
class ApachiiSkyHairFemale(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, ApachiiSkyHairFull()),)


@Singleton
class ApachiiSkyHairMale(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, ApachiiSkyHairFemale()),)


@Singleton
class ApachiiSkyHairNaturalRetexture(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, ApachiiSkyHairMale()),)


@Singleton
class DimonizedUNPFemaleBody(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, ApachiiSkyHairNaturalRetexture()),)


@Singleton
class AllInOneFacePackUNP(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, DimonizedUNPFemaleBody()),)


@Singleton
class RealGirlsRealisticBodyTextureUNP(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, AllInOneFacePackUNP()),)


@Singleton
class BetterMalesFace(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, RealGirlsRealisticBodyTextureUNP()),)


@Singleton
class BetterMalesBody(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, BetterMalesFace()),)


@Singleton
class HighDefinitionTeeth(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, BetterMalesBody()),)


# class SkySightSkinsHDMaleTextures(SkyrimMod):
#     def relationships(self):
#         return (modbase.Dependency(self, HighDefinitionTeeth()),)
@Singleton
class EyesOfBeauty(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, HighDefinitionTeeth()),)


@Singleton
class EyesOfBeautyNPC(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, EyesOfBeauty()),)


@Singleton
class RealisticRagdollsAndForce(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, EyesOfBeautyNPC()),)


# class EnhancedCharacterEdit(SkyrimMod):
#     def apply(self):
#         extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

###############################################################################
# Immersion mods
###############################################################################
@Singleton
class SkyUI5(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, RealisticRagdollsAndForce()),)


@Singleton
class InterestingNPCs(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, SkyUI5()),)


@Singleton
class WetAndColdRegularEdition(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, InterestingNPCs()),)


@Singleton
class WetAndColdAshes(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, WetAndColdRegularEdition()),)


@Singleton
class CompleteCampingSystem(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, WetAndColdAshes()),)


@Singleton
class Tentapalooza(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, CompleteCampingSystem()),)


@Singleton
class FrostfallSurvival(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, Tentapalooza()),)


@Singleton
class RealisticNeedsAndDiseases(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, FrostfallSurvival()),)


@Singleton
class ImmersivePatrols(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, RealisticNeedsAndDiseases()),)


@Singleton
class TouringCarriages(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, ImmersivePatrols()),)


@Singleton
class LanternsOfSkyrim(SkyrimMod):
    def dependencies(self):
        return (modbase.Dependency(self, TouringCarriages()),)


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
