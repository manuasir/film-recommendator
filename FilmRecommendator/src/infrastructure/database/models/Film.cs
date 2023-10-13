using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

namespace Models
{
    public class Film
    {
        [BsonId]
        [BsonRepresentation(BsonType.ObjectId)]
        public string Id { get; set; } // Unique identifier for the film document

        [BsonElement("Title")]
        public string Title { get; set; } // Title of the film

        [BsonElement("Year")]
        public int Year { get; set; } // Year of release for the film

        [BsonElement("Director")]
        public string Director { get; set; } // Name of the film's director

        [BsonElement("Genre")]
        public string Genre { get; set; } // Genre of the film

        [BsonElement("Summary")]
        [BsonIgnoreIfNull]
        public string Summary { get; set; }
        // Summary of the film (optional); marked as potentially optional with [BsonIgnoreIfNull]

        // Additional properties or methods for the Film class can be added here.
    }
}
