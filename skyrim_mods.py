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
    def run_post_processing(self):
        log.info("Running 'Textures Install.vbs'")
        install_script = "{0}/Textures Install.vbs".format(appconfig.SKYRIM_DATA_DIRECTORY)
        if os.path.exists(install_script):
            subprocess.call(["cscript.exe", install_script])

class UnofficialHighResolutionPatch(SkyrimMod):

    def relationships(self):
        return (modbase.Dependency(self, OptimizedVanillaTextures()),)

class UnofficialSkyrimPatch(SkyrimMod):

    def relationships(self):
        return (modbase.Dependency(self, UnofficialHighResolutionPatch()),)

class UnofficialSkyrimLegendaryEditionPatch(SkyrimMod):

    def relationships(self):
        return (modbase.Dependency(self, UnofficialHighResolutionPatch()),)

class StaticMeshImprovementMod(SkyrimMod):

    # TODO: This can have a dependency on either Unofficial Skyrim Patch or
    # TODO: UnofficialSkyrimLegendaryEditionPatch. How to resolve?
    def relationships(self):
        return (modbase.Dependency(self, UnofficialSkyrimPatch()),)

class RuinsClutterImproved(SkyrimMod):

    def relationships(self):
        return (modbase.Dependency(self, StaticMeshImprovementMod()),)

class AlternateStart(SkyrimMod):

    def relationships(self):
        return (modbase.Dependency(self, RuinsClutterImproved()),)

class CinematicFireEffects(SkyrimMod):

    def relationships(self):
        return (modbase.Dependency(self, AlternateStart()),)

class HDEnhancedTerrain(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, CinematicFireEffects()),)

class SkyrimDistanceOverhaul(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, HDEnhancedTerrain()),)

class SkyrimDistanceOverhaulSkymillsPatch(SkyrimMod):
    # TODO: Patches should be a part of main mod. How to resolve?
    def relationships(self):
        return (modbase.Dependency(self, SkyrimDistanceOverhaul()),)

class AnimatedDistantWaterfallsAndWindmills(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, SkyrimDistanceOverhaulSkymillsPatch()),)

class SkyrimHDFullVersion(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, AnimatedDistantWaterfallsAndWindmills()),)

class SkyrimCityBeautificationAllInOneByJK(SkyrimMod):
    def apply(self):
        #extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))
        # TODO: Come back to this mod. Seems like nexus is downloading incorrect archive size.
        pass

class VividLandscapesDungeonsAndRuins(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, SkyrimHDFullVersion()),)

    # TODO: Move to configuration function?
    def run_post_processing(self):
        upsert_configuration(r"SkyrimPrefs.ini", {"bDeferredShadows": 1})
        upsert_configuration(r"enblocal.ini", {"FixParallaxBugs": True})

class VividLandscapesDungeonsAndRuinsSMIMPatch(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, VividLandscapesDungeonsAndRuins()),)

class VividLandscapesVolcanicArea(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, VividLandscapesDungeonsAndRuinsSMIMPatch()),)

class AMidianBornCavesAndMines2k(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, VividLandscapesVolcanicArea()),)

class ImmersiveRoads(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, AMidianBornCavesAndMines2k()),)

    def run_post_processing(self):
        upsert_configuration(r"enblocal.ini", {"FixParallaxBugs": True})

class ImmersiveRoadsSnowShinePatch(SkyrimMod):
    # TODO: May not need this. Snow too dark.
    def apply(self):
        extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

class SkyrimFloraOverhaul(SkyrimMod):

    # TODO: Patch above isn't used. If desired, this dependency needs to be updated.
    def relationships(self):
        return (modbase.Dependency(self, ImmersiveRoads()),)

class SkyrimFloraOverhaulTallPines(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, SkyrimFloraOverhaul()),)

class TreesHD(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, SkyrimFloraOverhaulTallPines()),)

class SimplyBiggerTrees(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, TreesHD()),)

class SimplyBiggerTreesSlowerBranches(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, SimplyBiggerTrees()),)

class ParallaxTreebark4K(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, SimplyBiggerTreesSlowerBranches()),)

class ParallaxTreebark4KSimplyBiggerTreesPatch(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, ParallaxTreebark4K()),)

class ImmersiveFallenTrees(SkyrimMod):

    # TODO: This dependency is purely for flow of install. Clearly this isn't a
    # TODO: dependency of this mod. Need to redesign.
    def relationships(self):
        return (modbase.Dependency(self, ParallaxTreebark4KSimplyBiggerTreesPatch()),)

class FencesOfSkyrim(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, ImmersiveFallenTrees()),)

class RusticWindows2K(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, FencesOfSkyrim()),)

class VerdantGrassPlugin(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, RusticWindows2K()),)

    def run_post_processing(self):
        upsert_configuration(r"Skyrim.ini", {"iMaxGrassTypesPerTexure": 15}) #TODO: Add [Grass] section
        upsert_configuration(r"Skyrim.ini", {"iMinGrassSize": 60})

class VerdantGrassPluginDarkGrassTextureOption(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, VerdantGrassPlugin()),)

class NaturalGrassTextureFloor(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, VerdantGrassPluginDarkGrassTextureOption()),)

class RealVisionFloraPatch(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, NaturalGrassTextureFloor()),)

class HighDefinitionIvy2K(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, RealVisionFloraPatch()),)

class DetailedRugs(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, HighDefinitionIvy2K()),)

class PureWatersLegendaryEdition(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, DetailedRugs()),)

class PureWatersLandscapeTextures(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, PureWatersLegendaryEdition()),)

class VividLandscapesRockingStonesParallax(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, PureWatersLandscapeTextures()),)

class VividLandscapesCliffsAndCreeks(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, VividLandscapesRockingStonesParallax()),)

class VividLandscapesRockingStonesCompatibilityPatch(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, VividLandscapesCliffsAndCreeks()),)

class VividLandscapesTundraMossRevisited(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, VividLandscapesRockingStonesCompatibilityPatch()),)

class VividLandscapesTundraSMIMPatch(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, VividLandscapesTundraMossRevisited()),)

class VividLandscapesTundraMossMountainPatch(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, VividLandscapesTundraSMIMPatch()),)

class FinerDust(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, VividLandscapesTundraMossMountainPatch()),)

class RealisticSmokeAndEmbers(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, FinerDust()),)

# TODO: Remove fake mod
class FakeMod(SkyrimMod):
    pass

class ParticlePatchForENB(SkyrimMod):

    def relationships(self):
        return (modbase.Dependency(self, RealisticSmokeAndEmbers()),
                modbase.Superiority(self, StaticMeshImprovementMod()))

class SubsurfaceScatteringPatchForENB(SkyrimMod):

    def relationships(self):
        return (modbase.Dependency(self, ParticlePatchForENB()),
                modbase.Superiority(self, StaticMeshImprovementMod()))

class ParallaxTerrain4K(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, SubsurfaceScatteringPatchForENB()),)

class CoastBeachTexturesForParallax(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, ParallaxTerrain4K()),)

class PineForestTexturesForParallax(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, CoastBeachTexturesForParallax()),)

class ClimatesOfTamriel(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, PineForestTexturesForParallax()),)

class ClimatesOfTamrielSupremeStorms(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, ClimatesOfTamriel()),)

class ClimatesOfTamrielWeatherPatch(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, ClimatesOfTamrielSupremeStorms()),)

class TrueStorms(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, ClimatesOfTamrielWeatherPatch()),)

class RealisticLightingOverhaul(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, TrueStorms()),)

class LanternsOfSkyrim(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, RealisticLightingOverhaul()),)


# TODO: Separate Enb out from Skyrim-specific mod
class EnbSeriesV308(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, LanternsOfSkyrim()),)

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

    def relationships(self):
        return (modbase.Dependency(self, EnbSeriesV308()),)

class RealVisionFloraPatch(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, RealVisionENB()),)


###############################################################################
# Model mods
###############################################################################
class ShowRaceMenuPrecacheKiller(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, RealVisionFloraPatch()),)

class XeniusCharacterEnhancementFull(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, ShowRaceMenuPrecacheKiller()),)

class ApachiiSkyHairFull(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, XeniusCharacterEnhancementFull()),)

class ApachiiSkyHairFemale(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, ApachiiSkyHairFull()),)

class ApachiiSkyHairMale(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, ApachiiSkyHairFemale()),)

class ApachiiSkyHairNaturalRetexture(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, ApachiiSkyHairMale()),)

class DimonizedUNPFemaleBody(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, ApachiiSkyHairNaturalRetexture()),)

class AllInOneFacePackUNP(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, DimonizedUNPFemaleBody()),)

class RealGirlsRealisticBodyTextureUNP(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, AllInOneFacePackUNP()),)

class BetterMalesFace(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, RealGirlsRealisticBodyTextureUNP()),)

class BetterMalesBody(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, BetterMalesFace()),)

class HighDefinitionTeeth(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, BetterMalesBody()),)

# class SkySightSkinsHDMaleTextures(SkyrimMod):
#     def relationships(self):
#         return (modbase.Dependency(self, HighDefinitionTeeth()),)

class EyesOfBeauty(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, HighDefinitionTeeth()),)

class EyesOfBeautyNPC(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, EyesOfBeauty()),)

class RealisticRagdollsAndForce(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, EyesOfBeautyNPC()),)

# class EnhancedCharacterEdit(SkyrimMod):
#     def apply(self):
#         extract_to_skyrim_data_folder(compressed_file(self.__class__.__name__))

###############################################################################
# Immersion mods
###############################################################################

class SkyUI5(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, RealisticRagdollsAndForce()),)

class InterestingNPCs(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, SkyUI5()),)

class WetAndColdRegularEdition(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, InterestingNPCs()),)

class WetAndColdAshes(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, WetAndColdRegularEdition()),)

class CompleteCampingSystem(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, WetAndColdAshes()),)

class Tentapalooza(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, CompleteCampingSystem()),)

class FrostfallSurvival(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, Tentapalooza()),)

class RealisticNeedsAndDiseases(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, FrostfallSurvival()),)

class ImmersivePatrols(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, RealisticNeedsAndDiseases()),)

class TouringCarriages(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, ImmersivePatrols()),)

class LanternsOfSkyrim(SkyrimMod):
    def relationships(self):
        return (modbase.Dependency(self, TouringCarriages()),)


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
