from tables.basic_calc_table import Base_Calc_Table

class NEIGHBOURHOOD_CALC_Table(Base_Calc_Table):
	"The definition of the Neighbourhood Calculations in the database"

	num_of_rows_to_leave = 1
	table_name = "NEIGHBOURHOOD_CALC_TABLE"
	columns = 	Base_Table.columns + ["AdairPark", "AdamsPark", "Adamsville",
									"AlmondPark", "AmalHeights", "AnsleyPark",
									"Arden", "Ardmore", "ArgonneForest",
									"ArlingtonEstates", "AshleyCourts", "AshviewHeights",
									"AtkinsPark", "AtlantaIndustrialPark", "AtlantaUniversityCenter",
									"AtlanticStation", "AudobonForest", "AudobonForestWest", "BakerHills",
									"BakersFerry", "Bankhead", "Bankhead", "BankheadCourts", "BeecherHills",
									"BenHill", "BenHillAcres", "BenHillForest", "BenHillPines", "BenHillTerrace",
									"BenteenPark", "BerkleyPark", "BetmarLavilla", "BlairVilla", "Blandtown",
									"Bolton", "BoltonHills", "BoulderPark", "BoulevardHeights", "Brandon",
									"Brentwood", "BriarGlen", "Brookhaven", "BrookviewHeights", "Brookwood",
									"BrookwoodHills", "BrownsMillPark", "BuckheadForest", "BuckheadHeights",
									"BuckheadVillage", "BushMountain", "Butner", "Cabbagetown", "CampbelltonRoad",
									"CandlerPark", "CapitalGateway", "CapitolView", "CapitolViewManor", "CareyPark",
									"CarrollHeights", "CarverHills", "CascadeAvenue", "CascadeGreen", "CascadeHeights",
									"CastleberryHill", "Castlewood", "CenterHill", "ChaletWoods", "ChanningValley",
									"ChastainPark", "Chattahoochee", "ChosewoodPark", "CollierHeights", "CollierHills",
									"CollierHillsNorth", "ColonialHomes", "CrossCreek", "Custer Guice", "Deerwood",
									"DixieHills", "Downtown", "DruidHills", "EastAcresValley", "EastArdleyRoad",
									"EastAtlanta", "EastChastainPark", "EastLake", "Edgewood", "ElmcoEstates",
									"EnglewoodManor", "EnglishAvenue", "EnglishPark", "Fairburn", "FairburnHeights",
									"FairburnMays", "FairburnRoad", "FairburnTell", "FairwayAcres", "Fernleaf",
									"FloridaHeights", "FortMcPherson", "FortValley", "GardenHills", "GeorgiaTech",
									"GlenroseHeights", "GrantPark", "Greenbriar", "GreenbriarVillage", "GreenForestAcres",
									"GrovePark", "HammondPark", "HanoverWest", "HarlandTerrace", "HarrisChiles",
									"HarvelHomesCommunity", "HeritageValley", "HighPoint", "HillsPark", "HomePark",
									"HorseshoeCommunity", "HunterHills", "Huntington", "InmanPark", "IvanHill", "Joyland",
									"JustUs", "KingsForest", "Kingswood", "Kirkwood", "KnightPark", "LakeClaire", "LakeEstates",
									"Lakewood", "LakewoodHeights", "LaurensValley", "LeilaValley", "Lenox", "LincolnHomes",
									"Lindbergh", "Lindridge", "LoringHeights", "MagnumManor", "MargaretMitchell",
									"MariettaStreetArtery", "Mays", "MeadowbrookForest", "Mechanicsville", "Mellwood",
									"MemorialPark", "Midtown", "MidwestCascade", "MonroeHeights", "Morningside", "MozleyPark",
									"MtGileadWoods", "MtParanNside", "MtParanPkwy", "NiskeyCovve", "NiskeyLake", "NorthBuckhead",
									"NorwoodManor", "Oakcliff", "Oakland", "OaklandCity", "OldFairburnVillage", "OldFourthWard",
									"OldGordon", "OrchardKnob", "OrmewoodPark", "Paces", "PeachtreeBattleAlliance",
									"PeachtreeHeightsEast", "PeachtreeHeightsWest", "PeachtreeHills", "PeachtreePark",
									"PenelopeNeighbors", "Peoplestown", "Perkerson", "PeytonForest", "PiedmontHeights", "PineHills",
									"Pittsburgh", "PleasantHill", "PolarRock", "PomonaPark", "PonceyHighland", "PrincetonLakes",
									"RandallMill", "RebelValleyForest", "RegencyTrace", "Reynoldstown", "RidgecrestForest",
									"RidgedalePark", "RidgewoodHeights", "Riverside", "Rockdale", "RosedaleHeights", "RueRoyal",
									"SandlewoodEstates", "ScottsCrossing", "SherwoodForest", "SouthAtlanta", "SouthRiverGardens",
									"SouthTuxedoPark", "Southwest", "Springlake", "StateFacility", "Summerhill", "SwallowCircle",
									"SweetAuburn", "SylvanHills", "TampaPark", "ThomasvilleHeights", "TuxedoPark", "UnderwoodHills",
									"VenetianHills", "VillageCarver", "VillagesCastleberryHill", "VillagesEastLake", "VineCity",
									"VirginiaHighland", "WashingtonPark", "WesleyBattle", "WestEnd", "Westhaven", "WestHighland",
									"WestLake", "WestManor", "Westminster", "WestoverPlantation", "WestPacesFerrry", "Westview",
									"WestwoodTerrace", "WhitewaterCreek", "WhittierMillVillage", "Wildwood", "Wildwood",
									"WildwoodForest", "WilsonMillMeadows", "WisteriaGardens", "Woodfield", "WoodlandHills", "Wyngate"]

	def __init__(self) :
		Base_Table.__init__()
