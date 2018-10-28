package questions

import org.apache.spark.sql.SparkSession
import org.apache.spark.rdd.RDD
import org.apache.spark.SparkConf
import scala.math._

import org.apache.spark.graphx._
import org.apache.spark.graphx.Edge
import org.apache.spark.graphx.Graph


/** GeoProcessor provides functionalites to
  * process country/city/location data.
  * We are using data from http://download.geonames.org/export/dump/
  * which is licensed under creative commons 3.0 http://creativecommons.org/licenses/by/3.0/
  *
  * @param spark reference to SparkSession
  * @param filePath path to file that should be modified
  */
class GeoProcessor(spark: SparkSession, filePath:String) {

  //read the file and create an RDD
  //DO NOT EDIT
  val file = spark.sparkContext.textFile(filePath)

  /** filterData removes unnecessary fields and splits the data so
    * that the RDD looks like RDD(Array("<name>","<countryCode>","<dem>"),...))
    * Fields to include:
    *   - name (element 1 (2nd))
    *   - countryCode (element 8)
    *   - dem (digital elevation model) (element 16)
    *
    * @return RDD containing filtered location data. There should be an Array for each location
    */
  def filterData(data: RDD[String]): RDD[Array[String]] = {
    /* hint: you can first split each line into an array.
    * Columns are separated by tab ('\t') character.
    * Finally you should take the appropriate fields.
    * Function zipWithIndex might be useful.
    */
    val splitRdd = data.map {
      s =>
        val a = s.split("\t")
        val arrayInside = Array(a(1), a(8), a(16))
        arrayInside
    }

    splitRdd
  }


  /** filterElevation is used to filter to given countryCode
    * and return RDD containing only elevation(dem) information
    *
    * @param countryCode code e.g(AD)
    * @param data an RDD containing multiple Array[<name>, <countryCode>, <dem>]
    * @return RDD containing only elevation information
    */
  def filterElevation(countryCode: String,data: RDD[Array[String]]): RDD[Int] = {
    // https://stackoverflow.com/questions/39727964/converting-string-rdd-to-int-rdd
    val selection = data.filter(s => s.contains(countryCode))
    val dem = selection.map(array => (array(2))) // Array[String] = Array(2860, 2803)
    val res = dem.map(_.toInt)
    res
  }

  /** elevationAverage calculates the elevation(dem) average
    * to specific dataset.
    *
    * @param data: RDD containing only elevation information
    * @return The average elevation
    */
  def elevationAverage(data: RDD[Int]): Double = {
    val accum = spark.sparkContext.longAccumulator("elevationAverageAccumulator")
    data.foreach(x => accum.add(x))
    val res = accum.avg
    res
  }

  /** mostCommonWords calculates what is the most common
    * word in place names and returns an RDD[(String,Int)]
    * You can assume that words are separated by a single space ' '.
    *
    * @param data an RDD containing multiple Array[<name>, <countryCode>, <dem>]
    * @return RDD[(String,Int)] where string is the word and Int number of
    * occurrences. RDD should be in descending order (sorted by number of occurrences).
    * e.g ("hotel", 234), ("airport", 120), ("new", 12)
    */
  def mostCommonWords(data: RDD[Array[String]]): RDD[(String,Int)] = {
    val splitIt = data.flatMap { s =>  s(0).split(" ")}.map(word => (word,1))reduceByKey((a, b) => a + b)
    val count = splitIt.sortBy {case (k,v) => (-v,k)}
    count
  }

  /** mostCommonCountry tells which country has the most
    * entries in geolocation data. The correct name for specific
    * countrycode can be found from countrycodes.csv.
    *
    * @param data filtered geoLocation data
    * @param path to countrycode.csv file
    * @return most common country as String e.g Finland or empty string "" if countrycodes.csv
    *         doesn't have that entry.
    */
  def mostCommonCountry(data: RDD[Array[String]], path: String): String = {
    val splitIt = data.flatMap { s =>  s(1).split(" ")}.map(word => (word,1))reduceByKey((a, b) => a + b)
    val count = splitIt.sortBy {case (k,v) => (-v,k)}
    val countryCode = count.keys.first()
    val csvFile = spark.sparkContext.textFile(path)
    val csvData = csvFile.map(s => s.split(",")).filter(d => d.contains(countryCode))
    var result = ""

    if (csvData.isEmpty() == false) {
      result = csvData.map(s => s(0)).first()
    }

    result
  }

  /**
    * How many hotels are within 10 km (<=10000.0) from
    * given latitude and longitude?
    * https://en.wikipedia.org/wiki/Haversine_formula
    * earth radius is 6371e3 meters.
    *
    * Location is a hotel if the name contains the word 'hotel'.
    * Don't use feature code field!
    *
    * Important
    *   if you want to use helper functions, use variables as
    *   functions, e.g
    *   val distance = (a: Double) => {...}
    *
    * @param lat latitude as Double
    * @param long longitude as Double
    * @return number of hotels in area
    */
  def hotelsInArea(lat: Double, long: Double): Int = {
    //val linesWithSpark = textFile.filter(line => line.contains("Spark"))
    //val file = spark.sparkContext.textFile(getClass().getResource("/allCountries.txt").toString)
    val linesWithHotel = file.filter(line => line.toLowerCase.contains("hotel"))

    val haversineFormula =
      (hotelLatitude: Double, hotelLongitude: Double,
       reqLatitude: Double, reqLongitude: Double) => {
      val latDistance = Math.toRadians(hotelLatitude - reqLatitude)
      val longDistance = Math.toRadians(hotelLongitude - reqLongitude)
      val sinLat = Math.sin(latDistance / 2)
      val sinLng = Math.sin(longDistance / 2)
      val a = sinLat * sinLat +
        (Math.cos(Math.toRadians(hotelLatitude))
          * Math.cos(Math.toRadians(reqLatitude))
          * sinLng * sinLng)
      val c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a))
      (6371 * c)
    }

    val splitRdd = linesWithHotel.map{
      s => s.split("\t")
    }.filter{
      r =>
        val hotelLatitude = r(4).toDouble
        val hotelLongitude = r(5).toDouble
        val distance = haversineFormula(hotelLatitude, hotelLongitude, lat, long)
        if (distance <= 10.0) {
          true
        }
        else {
          false
        }
    }.map(a => Array(a(1)))

    val distinctHotel = splitRdd.map(a => a.toList).distinct()

    distinctHotel.count().toInt
  }

  //GraphX exercises

  /**
    * Load FourSquare social graph data, create a
    * graphx graph and return it.
    * Use user id as vertex id and vertex attribute.
    * Use number of unique connections between users as edge weight.
    * E.g
    * ---------------------
    * | user_id | dest_id |
    * ---------------------
    * |    1    |    2    |
    * |    1    |    2    |
    * |    2    |    1    |
    * |    1    |    3    |
    * |    2    |    3    |
    * ---------------------
    *         || ||
    *         || ||
    *         \   /
    *          \ /
    *           +
    *
    *         _ 3 _
    *         /' '\
    *        (1)  (1)
    *        /      \
    *       1--(2)--->2
    *        \       /
    *         \-(1)-/
    *
    * Hints:
    *  - Regex is extremely useful when parsing the data in this case.
    *  - http://spark.apache.org/docs/latest/graphx-programming-guide.html
    *
    * @param path to file. You can find the dataset
    *  from the resources folder
    * @return graphx graph
    *
    */
  def loadSocial(path: String): Graph[Int,Int] = {
    val file = spark.sparkContext.textFile(path)
    val spaceRemoved = file.map(s => s.replace(" ", ""))
    val selectedRow = spaceRemoved.filter(line => line.matches("""[0-9]+\|[0-9]+"""))
      .map(s => s.split('|')) //.map(_.toInt))

    val edgeValue = selectedRow.map(x => List(x(0).toInt, x(1).toInt))
    val v = edgeValue.map(x => (x, 1)).reduceByKey((a, b) => a + b)
    val res = v.map(p => Edge(p._1(0), p._1(1), p._2))

    val u: RDD[(VertexId, Int)] = selectedRow.flatMap(s => s).distinct().map(a => (a.toInt, a.toInt))

    Graph(u, res)
  }

  /**
    * Which user has the most outward connections.
    *
    * @param graph graphx graph containing the data
    * @return vertex_id as Int
    */
  def mostActiveUser(graph: Graph[Int,Int]): Int = {
    val group = graph.edges.groupBy(_.srcId)
    val followCount = group.map{
      case (vertex, edges) => (vertex, edges.map(_.attr).sum)
    }.collect
    val mostActiveUser = followCount.sortBy(- _._2).head

    mostActiveUser._1.toInt
  }

  /**
    * Which user has the highest pageRank.
    * https://en.wikipedia.org/wiki/PageRank
    *
    * @param graph graphx graph containing the data
    * @return user with highest pageRank
    */
  def pageRankHighest(graph: Graph[Int,Int]): Int = {
    val ranks = graph.pageRank(0.001).vertices
    ranks.sortBy(- _._2).first()._1.toInt
  }
}
/**
  *
  *  Change the student id
  */
object GeoProcessor {
  val studentId = "728214"
}