# Software_eng_lab1

# مدیریت نسخ پروژه و یکپارچه‌سازی مستمر

---

## روال انجام آزمایش

پروژه‌ی انتخاب‌شده برای این آزمایش، یک ماشین حساب ساده با قابلیت اجرای 6 عملیات محاسباتی به زبان پایتون است. برای فرایند توسعه با استفاده از ابزار گیت، ابتدا یک برنچ develop ساخته می‌شود و برای هر operation یک برنچ جدید روی develop با فرمت feat/operation_name ساخته می‌شود که پس از کامیت کردن تغییرات مد نظر برنچ، با pull request با برنچ develop مرج می‌شود.

---

## پرسش‌ها

علاوه بر گزارش آزمایش، پاسخ سوالات زیر را هم داخل فایل README بنویسید:

1. پوشه‌ی .git چیست؟ چه اطلاعاتی در آن ذخیره می‌شود؟ با چه دستوری ساخته می‌شود؟
   
   پوشه‌ی .git یک پوشه‌ی مخفی است که به طور خودکار هنگامی که یک مخزن Git را در یک پوشه با استفاده از دستور "git init" می‌سازیم، ایجاد می‌شود. این پوشه شامل تمام اطلاعات مورد نیاز برای کنترل نسخه (version control) است. برای مثال اگر بخواهیم مخزن خود را کلون کنیم، کافیست git. را کپی کنیم. این پوشه همچنین حاوی یک log است که تاریخچه‌ی commitها را ذخیره می‌کند. این log می‌تواند به ما کمک کند تا به نسخه‌ی مورد نظر از کدمان بازگردیم.
   
    برخی زیرپوشه‌ها و فایل‌هایی که در این پوشه یافت می‌شوند عبارتند از:    
   
   پوشه‌ی hooks: این پوشه حاوی فایل‌های اسکریپت است. Git hookها اسکریپت‌هایی هستند که قبل یا بعد از رویدادهایی مانند commit، push و غیره اجرا می‌شوند.    
   
   پوشه‌ی اشیاء: این پوشه یک پایگاه داده شی از Git را نشان می‌دهد.    
   
   فایل config: این فایل پیکربندی محلی است.    
   
   پوشه‌ی refs: این پوشه اطلاعات مربوط به برچسب‌ها و شاخه‌ها را ذخیره می‌کند.   
   
   فایل HEAD: این فایل ارجاعی به شاخه فعلی را ذخیره می‌کند. به طور پیش‌فرض به شاخه اصلی اشاره می‌کند.    
   
   فایل index: یک فایل باینری است و اطلاعات مرحله‌بندی را ذخیره می‌کند.
   
   همان‌طور که گفته‌شد، این پوشه با دستور git init در آن پوشه‌ای که این دستور وارد شده، ساخته می‌شود.

2. منظور از atomic بودن در atomic commit و atomic pull-request چیست؟
   
   در Git، منظور از atomic commit یک commit واحد است که شامل مجموعه‌ای از تغییرات است که از نظر منطقی مرتبط هستند و باید با هم اعمال شوند. atomic commit اغلب برای گروه‌بندی تغییراتی که مربوط به یک ویژگی خاص یا رفع اشکال هستند استفاده می‌شود و درک هدف و زمینه تغییرات را آسان‌تر می‌کند.
   
   کار با atomic commit به این معنی است که commitهای شما کوچک‌ترین اندازه ممکن را دارند. هر commit یک و فقط یک کار ساده انجام می‌دهد که می تواند در یک جمله‌ی ساده خلاصه شود. مقدار تغییر کد مهم نیست. می تواند یک حرف یا صد هزار خط باشد، اما شما باید بتوانید تغییر را با یک جمله کوتاه ساده توصیف کنید.

3. تفاوت دستورهای fetch و pull و merge و rebase را بیان کنید.

4. تفاوت چهار دستور reset و revert و restore را بیان کنید.

5. منظور از stage چیست؟ دستور stash چه کاری را انجام می‌دهد؟

6. مفهوم snapshot به چه معناست؟
