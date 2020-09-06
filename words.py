import pandas as pd
dictionary = [

    {
        "word": "Abrasives",
        "definition": "Зүлгүүр",
        "rel": ["Abrasive damage"]
    },
    {
        "word": "Abrasive damage",
        "definition": "Үрэлт/зүлгэлтийн гэмтэл, элэгдэл",
        "rel": ["Abrasives"]
    },

    {
        "word": "Accelerator",
        "definition": "Хааз",
        "rel": ["Acceleration"]
    },
    {
        "word": "Actuate",
        "definition": "Хөдөлгөх, ажиллуулах, өдөөх, ажиллах",
        "rel": ["Actuator"]
    },
    {
        "word": "Adjust",
        "definition": "тохируулах, засах, тааруулах",
        "rel": ["Adjustable fork", "Adjustable plier", "Adjustable wrench"]
    },
    {
        "word": "Adjustable fork",
        "definition": "сэрээ хэлбэрийн хавчигч",
        "rel": ["Adjustable plier", "Adjustable wrench"]
    },
    {
        "word": "Adjustable plier",
        "definition": "Хэрээн хошуут бахь",
        "rel": ["Adjustable wrench", "Adjustable fork"]
    },

    {
        "word": "Adjustable wrench",
        "definition": "пранцус, тохируулагч түлхүүр",
        "rel": ["Adjustable fork", "Adjustable plier", ]
    },
    {
        "word": "Aftercooler",
        "definition": "Дулааны нэмэгдэл хөргүүр, гүйцэд хөргөөгч",
        "rel": [""]
    },

    {
        "word": "Align",
        "definition": "зэрэгцүүлэх, эгнүүлэх, нэг эгнээ болгох",
        "rel": ["Aligning punch", "Alignment", "Alignment fixture"]
    },
    {
        "word": "Aligning punch",
        "definition": "Тааруулж, тохируулагч цоолтуур",
        "rel": ["Alignment", "Alignment fixture"]
    },

    {
        "word": "Alignment",
        "definition": "Тааруулах, тохируулах, байрлуулах",
        "rel": ["Alignment fixture"]
    },
    {
        "word": "Alignment fixture",
        "definition": "Тохиргоо хийх хэрэгсэл",
        "rel": ["Align", "Alignment"]
    },

    {
        "word": "Allen wrench",
        "definition": "6 талтай түлхүүр",
        "rel": [""]
    },
    {
        "word": "Alloy",
        "definition": "Хайлш, хайлгах, сайжруулагч элемент, сайжруулалт, бэхжүүлэлт",
        "rel": ["Alloy  steel"]
    },

    {
        "word": "Alloy  steel",
        "definition": "Сайжруулсан ган",
        "rel": ["Alloy"]
    },
    {
        "word": "Alter",
        "definition": "Өөр болох, өөрчлөгдөх, хувирах",
        "rel": ["Alternating current"]
    },

    {
        "word": "Alternating current",
        "definition": "Хувьсах гүйдэл",
        "rel": ["Alternator", "Alter"]
    },
    {
        "word": "Alternator",
        "definition": "Хувьсах гүйдлийн (синхрон) хам хөдөлгүүр/жанам",
        "rel": ["Alter"]
    },

    {
        "word": "Anneal",
        "definition": "шатаах, хатууруулах, давтах",
        "rel": [""]
    },
    {
        "word": "Armour glass",
        "definition": "Хагардаггүй шил",
        "rel": [""]
    },

    {
        "word": "Assembly",
        "definition": "Угсралт, иж бүрдэл",
        "rel": ["Bridge assembly"]
    },
    {
        "word": "Balance",
        "definition": "тэнцвэр, тэнцүүлэх",
        "rel": ["Balance machine", "Balance pad", "Balance shaft"]
    },

    {
        "word": "Balance machine",
        "definition": "Тэнцвэржүүлэх машин(хэрэгсэл), төхөөрөмж",
        "rel": ["Balance pad", "Balance shaft"]
    },
    {
        "word": "Balance pad",
        "definition": "Тогтворжуулах ивүүр",
        "rel": ["Balance", "Balance shaft"]
    },

    {
        "word": "Ball peen hammer",
        "definition": "Модон иштэй алх",
        "rel": ["Hammer"]
    },
    {
        "word": "Bar",
        "definition": "Лоом",
        "rel": [""]
    },

    {
        "word": "Bead",
        "definition": "Бөмбөлөг, цагираг, цөн, ирмэг, хөвөө, мөр, тахир тохой, бөмбөлөг хэлбэртэй жижиг эд анги, гол, хайлгасан металлыг ширээх, гол нарийн залгаас гаргаж гагнах, ширээх, хажуу (дугуй, гадуур дугуйн), бөмбөлөг (хий, агаарын)",
        "rel": ["Bead blasting"]
    },
    {
        "word": "Bead blasting",
        "definition": "Бөмбөлөг, шарикаар цэвэрлэх (шилэн бөмбөлөг г.м.)",
        "rel": ["Bead"]
    },

    {
        "word": "Beam",
        "definition": "Дам нуруу",
        "rel": [""]
    },
    {
        "word": "Bearing",
        "definition": "Холхивч",
        "rel": ["Bearing insert", "Bearing lining", "Bearing shells"]
    },

    {
        "word": "Bearing insert",
        "definition": "Холхивчны оруулга",
        "rel": ["Bearing shells", "Bearing lining"]
    },
    {
        "word": "Bearing lining",
        "definition": "Холхивчны дотор",
        "rel": ["Bearing shells", "Bearing insert"]
    },

    {
        "word": "Bearing shells",
        "definition": "Холхивчны вкладыш",
        "rel": ["Bearing insert", "Bearing lining"]
    },
    {
        "word": "Bench",
        "definition": "Мөргөцөг",
        "rel": [""]
    },

    {
        "word": "Bend",
        "definition": "Тахийх, мурийх, махийх, нугарах",
        "rel": ["Bending stress"]
    },
    {
        "word": "Bending stress",
        "definition": "Тахийлтын хүчдэл, тахийлтын ачаалал(стресс)",
        "rel": ["Bend"]
    },

    {
        "word": "Bevel gear",
        "definition": "Шувтан араа",
        "rel": [""]
    },
    {
        "word": "Blade",
        "definition": "Ир, хурц үзүүр, далбан, хутга",
        "rel": ["Blade rod"]
    },

    {
        "word": "Blade rod",
        "definition": "Хутган шатун",
        "rel": [""]
    },
    {
        "word": "Blast",
        "definition": "Тэсрэлт, дэлбэрэлт",
        "rel": ["Bead blasting"]
    },

    {
        "word": "Bogie",
        "definition": "Тэргэнцэр, явах хэсэг(кран, экскаваторын), вагонцор",
        "rel": [""]
    },
    {
        "word": "Boom",
        "definition": "Сум",
        "rel": [""]
    },

    {
        "word": "Booster",
        "definition": "Өдөөгч, хүчлүүр, бустер",
        "rel": [""]
    },
    {
        "word": "Bore",
        "definition": "Цооног, Голч (цилиндрийн диаметр)",
        "rel": [""]
    },

    {
        "word": "Brake",
        "definition": "тоормоз",
        "rel": ["Brake spring plier", "Hand brake"]
    },
    {
        "word": "Brake spring plier",
        "definition": "Тоормосны пүрш авагч бахь",
        "rel": [""]
    },

    {
        "word": "Breakage",
        "definition": "Эвдрэл, гэмтэл, осол",
        "rel": [""]
    },
    {
        "word": "Bridge assembly",
        "definition": "Хөндлөн угсралт",
        "rel": [""]
    },
    {
        "word": "Bypass",
        "definition": "Тойролт, тойруу, эргэх, салаалга",
        "rel": [""]
    },
    {
        "word": "By-product",
        "definition": "Дагавар бүтээгдэхүүн (урвал, үйл ажиллагаа, явцын)",
        "rel": [""]
    },
    {
        "word": "Cable",
        "definition": "Татлага утас, утас, трос, канат, мяндсан оосор(трос)",
        "rel": ["Cablebolter"]
    },
    {
        "word": "Cablebolter",
        "definition": "Кабель боолтын машин",
        "rel": ["Cable"]
    },
    {
        "word": "Cable gland",
        "definition": "кабелийн жийргэвч",
        "rel": [""]
    },
    {
        "word": "Cam",
        "definition": "Гулсах гадаргуутай, түүгээрээ бусад эд ангитай хүрэлцэж өгөгдсөн зүй тогтоол бүхий өөрийн хөдөлгөөнийг дамжуулах үүрэгтэй хүрдэн хэлбэрийн нударган механизмын эд анги",
        "rel": ["Camshaft", "Cam follower", "Camshaft drive", "Camshaft sprocket"]
    },
    {
        "word": "Camshaft",
        "definition": "Нударгат гол (хувиарлах)",
        "rel": ["Cam", "Cam follower", "Camshaft drive", "Camshaft sprocket"]
    },
    {
        "word": "Cam follower",
        "definition": "Нударган голын хөтлөгдөгч механизм",
        "rel": ["Camshaft drive", "Camshaft sprocket"]
    },
    {
        "word": "Camshaft drive",
        "definition": "Хувиарлах голын хөтлөгч",
        "rel": ["Cam", "Cam follower", "Camshaft sprocket"]
    },
    {
        "word": "Camshaft sprocket",
        "definition": "Гинжит хөтлөгдөх дугуй",
        "rel": ["Camshaft", "Cam follower"]
    },
    {
        "word": "Cap",
        "definition": "Хушуувч, таглавч",
        "rel": [""]
    },
    {
        "word": "Capacity",
        "definition": "Багтаамж, хүчин чадал",
        "rel": [""]
    },
    {
        "word": "Carbon",
        "definition": "Хөө, Тортог",
        "rel": ["Carbon paper", "Carbon scraper"]
    },
    {
        "word": "Carbon paper",
        "definition": "Хортой цаас",
        "rel": [""]
    },
    {
        "word": "Carbon scraper",
        "definition": "Тортог хусагч(арилгагч)",
        "rel": ["Carbon"]
    },
    {
        "word": "Carburetor",
        "definition": "Дотоод шаталтын хөдөлгүүрийн тэжээлийн системд бензин ба агаар хольж, халуун хольц бий болгох, түүний зарцуулалтыг тохируулах зориулалттай тусгай хийцийн төхөөрөмж",
        "rel": [""]
    },
    {
        "word": "Casting",
        "definition": "Цутгалт, цутгамал",
        "rel": ["Cast iron"]
    },
    {
        "word": "Cast iron",
        "definition": "Цутгамал төмөр",
        "rel": [""]
    },
    {
        "word": "Chamber",
        "definition": "Өрөө, тасалгаа, шаталт",
        "rel": [""]
    },
    {
        "word": "Chamfer",
        "definition": "Мөгүү, гажилт, мөлүү, мөгүүг арилгах, хөвөө ирмэгийг дугуйлах, эргүүлэх, жижиг суваг, жижиг малтац",
        "rel": [""]
    },
    {
        "word": "Chassis",
        "definition": "Тээврийн хэрэгслийн шасси, каркас, арал",
        "rel": [""]
    },
    {
        "word": "Chisel",
        "definition": "Цүүц",
        "rel": [""]
    },
    {
        "word": "Clamp",
        "definition": "Хавчаар, баривч, даруулга",
        "rel": [""]
    },
    {
        "word": "Clearance",
        "definition": "Зайц, завсар",
        "rel": [""]
    },
    {
        "word": "Clutch",
        "definition": "авцуулах холбоо",
        "rel": [""]
    },
    {
        "word": "Collar",
        "definition": "Хүзүүвч, босоо амын мод эсвэл бетон цутгамал хүзүүвч хэсэг",
        "rel": [""]
    },
    {
        "word": "Combustible",
        "definition": "Асамхай, шатамхай",
        "rel": ["Combustion"]
    },
    {
        "word": "Combustion",
        "definition": "Шаталт",
        "rel": ["Combustible"]
    },
    {
        "word": "Component",
        "definition": "Бүрдэл хэсэг, эд анги",
        "rel": [""]
    },
    {
        "word": "Compression",
        "definition": "Шахалт, агшаах, дарах",
        "rel": ["Compression ignition", "Compressor"]
    },
    {
        "word": "Compression ignition",
        "definition": "Шахалтаар асаах",
        "rel": ["Compressor"]
    },
    {
        "word": "Compressor",
        "definition": "Шахуурга, нягтруулавч",
        "rel": ["Compression", "Compression ignition"]
    },
    {
        "word": "Condensation",
        "definition": "шингэлэх, усжих, хуримтлах",
        "rel": [""]
    },
    {
        "word": "Conductor",
        "definition": "Дамжуулагч",
        "rel": ["Conduit"]
    },
    {
        "word": "Conduit",
        "definition": "Дамжуулах хоолой",
        "rel": [""]
    },
    {
        "word": "Configuration",
        "definition": "бүтэц, хэлбэршил",
        "rel": [""]
    },
    {
        "word": "Connecting rod",
        "definition": "Сэжлүүр - Пистон буюу бүлүүрийн давших хөдөлгөөнийг (машины гулсалтыг) тахир голын хүзүүний эргэлдэх хөдөлгөөнд хувиргах эд анги",
        "rel": [""]
    },
    {
        "word": "Coolant",
        "definition": "Хөргөх шингэн",
        "rel": [""]
    },
    {
        "word": "Corrosion",
        "definition": "Эсэлдэх, зэв идэх, идэгдэх",
        "rel": ["Corrosion resistance", "Corrosive chemicals"]
    },
    {
        "word": "Corrosion resistance",
        "definition": "Зэврэлтийг эсэргүүцэх чадвар",
        "rel": ["Corrosive chemicals"]
    },
    {
        "word": "Corrosive chemicals",
        "definition": "Хүчиллэг, идэмхий химийн бодис",
        "rel": ["Corrosion"]
    },
    {
        "word": "Counterweight",
        "definition": "Тэнцвэржүүлэх ачаа, эсрэг ачаа, жин тэнцүүлэгч",
        "rel": [""]
    },
    {
        "word": "Coupling",
        "definition": "Баривч - төрөл бүрийн гол, татуурга, хоолой, кабель зэргийг залган, холбоосыг нь барьж байх тоног",
        "rel": [""]
    },
    {
        "word": "Crab winch",
        "definition": "дамарт эргүүлэг",
        "rel": [""]
    },
    {
        "word": "Debris",
        "definition": "хэлтэрхий, хаягдал, үртэс",
        "rel": [""]
    },
    {
        "word": "Deceleration",
        "definition": "Удаашруулах, тоормослох",
        "rel": [""]
    },
    {
        "word": "Deflect",
        "definition": "Хазайх, зөрөх, гажих, хотойх, хугалах, хугарах",
        "rel": ["Deflection", "Deflector"]
    },
    {
        "word": "Deflection",
        "definition": "Хазайлт (соронзон зүүний), хугарал, зөрөө, гажилт",
        "rel": ["Deflect", "Deflector"]
    },
    {
        "word": "Deflector",
        "definition": "Агаар, шингэн, дууны долгионы урсгалын чиглэл өөрчлөх байгууламж",
        "rel": ["Deflect", "Deflection"]
    },
    {
        "word": "Delay",
        "definition": "хойшлуулах, удаашруулах",
        "rel": [""]
    },
    {
        "word": "Degreaser",
        "definition": "Тосгүйжүүлэгч",
        "rel": [""]
    },
    {
        "word": "Dent ",
        "definition": "Хонхорхой, цөмөрхий, ором, хэрчлээс, огтлоос",
        "rel": [""]
    },
    {
        "word": "Deposit",
        "definition": "Тунац, тортог, хаг, өнгөр",
        "rel": [""]
    },

    {
        "word": "Depth ",
        "definition": "гүн, зузаан",
        "rel": [""]
    },
    {
        "word": "Deteriorate",
        "definition": "муудах, дордох, эвдрэх",
        "rel": [""]
    },
    {
        "word": "Detonation",
        "definition": "тэсрэлт, тэсрэл, дэлбэрэх",
        "rel": ["Detonator"]
    },
    {
        "word": "Detonator",
        "definition": "тэслүүр, тэслэвч",
        "rel": ["Detonation"]
    },
    {
        "word": "Die",
        "definition": "Хэвлүүр, тамгалах - бэлдэцийн уян налархайн хэв гажилтыг ашиглан даралтаар материалыг боловсруулах багаж, хэрэгсэл",
        "rel": ["Die stamp", "riveting die", "Die-Cast"]
    },
    {
        "word": "Die-Cast",
        "definition": "Төмөр хэвэнд цутгасан ",
        "rel": ["Die stamp", "riveting die"]
    }]

words = pd.DataFrame(dictionary)
