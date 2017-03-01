from applogger import ModiLogger
log = ModiLogger()

import appconfig
import modbase
from modbase import ModBase
import modcore
import os
import subprocess
from zipfile import ZipFile

class SkyrimMod(ModBase):
    pass


###############################################################################
# Environment/Graphic mods
###############################################################################
class OptimizedVanillaTextures(SkyrimMod):

    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))
        log.info("Running 'Textures Install.vbs'")
        install_script = "{0}/Textures Install.vbs".format(appconfig.SKYRIM_DATA_DIRECTORY)
        if os.path.exists(install_script):
            subprocess.call(["cscript.exe", install_script])

class UnofficialHighResolutionPatch(SkyrimMod):

    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class UnofficialSkyrimPatch(SkyrimMod):

    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class UnofficialSkyrimLegendaryEditionPatch(SkyrimMod):

    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class StaticMeshImprovementMod(SkyrimMod):

    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class RuinsClutterImproved(SkyrimMod):

    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class AlternateStart(SkyrimMod):

    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class CinematicFireEffects(SkyrimMod):

    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class HDEnhancedTerrain(SkyrimMod):

    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class SkyrimDistanceOverhaul(SkyrimMod):

    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class SkyrimDistanceOverhaulSkymillsPatch(SkyrimMod):

    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class AnimatedDistantWaterfallsAndWindmills(SkyrimMod):

    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class SkyrimHDFullVersion(SkyrimMod):

    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class SkyrimCityBeautificationAllInOneByJK(SkyrimMod):

    def apply(self):
        #extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))
        # TODO: Come back to this mod. Seems like nexus is downloading incorrect archive size.
        pass

class VividLandscapesDungeonsAndRuins(SkyrimMod):

    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))
        upsert_configuration(r"SkyrimPrefs.ini", {"bDeferredShadows": 1})
        upsert_configuration(r"enblocal.ini", {"FixParallaxBugs": True})

class VividLandscapesDungeonsAndRuinsSMIMPatch(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class VividLandscapesVolcanicArea(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class AMidianBornCavesAndMines2k(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class ImmersiveRoads(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))
        upsert_configuration(r"enblocal.ini", {"FixParallaxBugs": True})

class ImmersiveRoadsSnowShinePatch(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class SkyrimFloraOverhaul(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class SkyrimFloraOverhaulTallPines(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class TreesHD(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class SimplyBiggerTrees(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class SimplyBiggerTreesSlowerBranches(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class ParallaxTreebark4K(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class ParallaxTreebark4KSimplyBiggerTreesPatch(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class ImmersiveFallenTrees(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class FencesOfSkyrim(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class RusticWindows2K(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class VerdantGrassPlugin(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))
        upsert_configuration(r"Skyrim.ini", {"iMaxGrassTypesPerTexure": 15}) #TODO: Add [Grass] section
        upsert_configuration(r"Skyrim.ini", {"iMinGrassSize": 60})

class VerdantGrassPluginDarkGrassTextureOption(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class NaturalGrassTextureFloor(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class RealVisionFloraPatch(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class HighDefinitionIvy2K(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class DetailedRugs(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class PureWatersLegendaryEdition(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class PureWatersLandscapeTextures(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class VividLandscapesRockingStonesParallax(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class VividLandscapesCliffsAndCreeks(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class VividLandscapesRockingStonesCompatibilityPatch(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class VividLandscapesTundraMossRevisited(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class VividLandscapesTundraSMIMPatch(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class VividLandscapesTundraMossMountainPatch(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class FinerDust(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class RealisticSmokeAndEmbers(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class ParticlePatchForENB(SkyrimMod):

    def relationships(self):
        return ( #modbase.Dependency(self, RealisticSmokeAndEmbers()),
                 modbase.Superiority(self, StaticMeshImprovementMod()) )

class SubsurfaceScatteringPatchForENB(SkyrimMod):

    def relationships(self):
        return ( modbase.Dependency(self, ParticlePatchForENB()),
                 modbase.Superiority(self, StaticMeshImprovementMod()) )

class ParallaxTerrain4K(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class CoastBeachTexturesForParallax(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class PineForestTexturesForParallax(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class ClimatesOfTamriel(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class ClimatesOfTamrielSupremeStorms(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class ClimatesOfTamrielWeatherPatch(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class TrueStorms(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class RealisticLightingOverhaul(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class LanternsOfSkyrim(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))


# TODO: Separate Enb out from Skyrim-specific mod
class EnbSeriesV308(SkyrimMod):
    def apply(self):
        extract_to_skyrim_base_folder(compressed_file(self.__class__.__name__))

class RealVisionENB(SkyrimMod):
    def apply(self):
        # TODO: After this extraction runs, need to run installer for realvision.
        # TODO: Make specified file modification under RealVision ENB manual install.
        extract_to_skyrim_base_folder(compressed_file(self.__class__.__name__))

class RealVisionFloraPatch(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))


###############################################################################
# Model mods
###############################################################################
class ShowRaceMenuPrecacheKiller(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class XeniusCharacterEnhancementFull(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class ApachiiSkyHairFull(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class ApachiiSkyHairFemale(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class ApachiiSkyHairMale(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class ApachiiSkyHairNaturalRetexture(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class DimonizedUNPFemaleBody(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class AllInOneFacePackUNP(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class NoMoreBlockyFaces(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class RealGirlsRealisticBodyTextureUNP(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class BetterMalesFace(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class BetterMalesBody(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class HighDefinitionTeeth(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class SkySightSkinsHDMaleTextures(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class EyesOfBeauty(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class EyesOfBeautyNPC(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class RealisticRagdollsAndForce(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class XVisionChildrenFixBubbleFace(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class EnhancedCharacterEdit(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

###############################################################################
# Immersion mods
###############################################################################

class SkyUI5(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class InterestingNPCs(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class WetAndColdRegularEdition(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class WetAndColdAshes(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class CompleteCampingSystem(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class Tentapalooza(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class FrostfallSurvival(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class RealisticNeedsAndDiseases(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class ImmersivePatrols(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class TouringCarriages(SkyrimMod):
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))


###############################################################################
#   Helper functions
###############################################################################
# todo: Is this needed after modcore changes?
def compressed_file(mod_name):
    return modcore.compressed_file(appconfig.SKYRIM_APP_MOD_DIRECTORY, mod_name)

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
