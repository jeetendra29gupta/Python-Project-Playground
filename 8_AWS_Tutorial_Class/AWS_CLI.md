## 🔰 **1. Bucket Operations**

### 📦 List All Buckets

Lists all buckets in your AWS account.

```bash
aws s3 ls
```

---

### 📦 Create a Bucket

Creates a new bucket. Bucket name must be globally unique.

```bash
aws s3 mb s3://my-bucket-name
```

### 📦 Create a Bucket in a Specific Region

Recommended: Create bucket in a specified AWS region.

```bash
aws s3 mb s3://my-bucket-name --region us-west-2
```

---

### 📦 Delete an Empty Bucket

Removes an **empty** bucket.

```bash
aws s3 rb s3://my-bucket-name
```

### 📦 Forcibly Delete a Bucket (With Contents)

Deletes the bucket and **all its objects**.

```bash
aws s3 rb s3://my-bucket-name --force
```

---

## 📄 **2. Object (File) Operations**

### 📄 Upload a File

```bash
aws s3 cp file.txt s3://my-bucket-name/
```

### 📄 Upload a Folder Recursively

```bash
aws s3 cp /local/folder s3://my-bucket-name/folder --recursive
```

---

### 📥 Download a File

```bash
aws s3 cp s3://my-bucket-name/file.txt ./localfile.txt
```

---

### 🚚 Move a File (Upload & Delete Local)

```bash
aws s3 mv localfile.txt s3://my-bucket-name/
```

### 🚚 Move File Between Buckets

```bash
aws s3 mv s3://source-bucket/file.txt s3://destination-bucket/
```

---

### ❌ Delete a File (Object)

```bash
aws s3 rm s3://my-bucket-name/file.txt
```

### ❌ Delete All Objects in a Bucket

```bash
aws s3 rm s3://my-bucket-name --recursive
```

---

## 🔍 **3. Listing Files and Details**

### 🔍 List Objects in Root of a Bucket

```bash
aws s3 ls s3://my-bucket-name/
```

### 🔍 List All Objects Recursively with Human-Readable Size

```bash
aws s3 ls s3://my-bucket-name/ --recursive --human-readable --summarize
```

---

## 🔄 **4. Synchronization**

### 🔄 Sync Local Folder to S3 Bucket

```bash
aws s3 sync ./local-folder s3://my-bucket-name/folder
```

### 🔄 Sync S3 to Local

```bash
aws s3 sync s3://my-bucket-name/folder ./local-folder
```

### 🔄 Sync and Delete Extra Files in Bucket

```bash
aws s3 sync ./local-folder s3://my-bucket-name/folder --delete
```

---

## 🌐 **5. Static Website Hosting**

### 🌐 Enable Static Website Hosting

```bash
aws s3 website s3://my-bucket-name/ --index-document index.html --error-document error.html
```
Website URL: `http://my-bucket-name.s3-website-<region>.amazonaws.com`

---

## 🔐 **6. Generate Pre-Signed URL (Temporary Access)**

### 🔐 Default (1 Hour Expiry)

```bash
aws s3 presign s3://my-bucket-name/file.txt
```

### 🔐 Custom Expiry (in seconds)

```bash
aws s3 presign s3://my-bucket-name/file.txt --expires-in 300
```

---

## 💡 **Bonus Tips**

### 🧠 Use `--dryrun` to Preview Without Action

```bash
aws s3 cp file.txt s3://my-bucket-name/ --dryrun
```

### 🔒 Apply Bucket Policy via JSON

```bash
aws s3api put-bucket-policy --bucket my-bucket-name --policy file://policy.json
```

### 🔄 Copy Between Buckets

```bash
aws s3 cp s3://bucket1/file.txt s3://bucket2/ --recursive
```

---

## 🧪 **Practice Ideas for Going Hero Mode**

1. 🔧 Create and delete test buckets in various regions.
2. 📥 Upload and download files using `cp`, `mv`, and `sync`.
3. 🌐 Host a basic HTML site from S3.
4. 🔐 Generate and test pre-signed URLs.
5. 🧹 Write scripts to clean up and archive buckets.

---

## 📚 AWS S3 CLI Reference

* [AWS CLI S3 Command Reference (Official)](https://docs.aws.amazon.com/cli/latest/reference/s3/index.html)
* [AWS CLI S3API for Advanced Options](https://docs.aws.amazon.com/cli/latest/reference/s3api/index.html)

---
