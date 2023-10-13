using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

namespace Models
{
    public class Film
    {
        [BsonId]
        [BsonRepresentation(BsonType.ObjectId)]
        public string Id { get; set; }

        [BsonElement("Title")]
        public string Title { get; set; }

        [BsonElement("Year")]
        public int Year { get; set; }

        [BsonElement("Director")]
        public string Director { get; set; }

        [BsonElement("Genre")]
        public string Genre { get; set; }

        [BsonElement("Summary")]
        public string Summary { get; set; }
    }
}
